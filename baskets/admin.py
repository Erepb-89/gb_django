from django.contrib import admin
from .models import Basket

# Register your models here.
admin.site.register(Basket)

# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     fields = ('user', 'product', 'quantity', 'created_timestamp', 'update_timestamp')
#     readonly_fields = ('created_timestamp', 'update_timestamp')
