from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(
                              OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'personal', 'id', 'photo_200')),
                                          access_token=response['access_token'],
                                          v='5.131')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    if data['personal']['langs']:
        user.userprofile.langs = ' '.join(data['personal']['langs'])

    if data['id']:
        user.userprofile.userid = f"vk.com/id{data['id']}"

    if data['photo_200']:
        photo_path = f'users_image/{user.pk}.jpg'
        with open(f'media/{photo_path}', 'wb') as photo:
            photo.write(requests.get(data['photo_200']).content)
        user.image = photo_path

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

    age = (timezone.now().date() - bdate).days // 365
    user.age = age
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.save()
