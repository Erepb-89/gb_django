// window.onload = function () {
//     $('.basket_list').on('click', 'input[type="number"]', function () {
//
//         let t_href = event.target;
//         console.log(t_href.name);
//         console.log(t_href.value);
//
//         $.ajax({
//             url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
//             success: function (data) {
//                 $('.basket_list').html(data.result)
//             },
//         });
//         event.preventDefault();
//     })
// }

window.onchange = function () {
    let basketList = document.querySelector('.basket_list');
    let inputs = document.querySelectorAll("[type='number']");

    inputs.forEach(input => {
        input.addEventListener('click', buttonClickHandler);
    });

    function buttonClickHandler(event) {
        let t_href = event.target;

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                basketList.innerHTML = '';
                basketList.insertAdjacentHTML('afterbegin', data.result);
            }
        });
        event.preventDefault();
    }
}



