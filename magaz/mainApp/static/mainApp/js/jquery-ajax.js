// СОЗДАЕМ ПУСТОЙ БЛОК
var emptyBlock = $('<h4>', {
    text: 'Пусто',
    style: 'text-align: center; margin-top: 2%;'
});
// ПОЛУЧАЕМ КУКИ (csrf)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// При нажатии на +

$('.increment').on('click', function() {
    const button = $(this);
    const productId = button.data('product');
    const quantity = button.data('quantity');
    const action = $(this).data('action');
    console.log('Отправка данных на сервер: productId =', productId, ', quantity =', quantity,'action', action);
    addToCartWithJQuery(productId, quantity, button, action);
});
// AJAX
function addToCartWithJQuery(productId, quantity, button, action) {
    $.ajax({
        url: 'http://127.0.0.1:8000/purchase/cart/',
        type: 'POST',
        data: {
            'product_id': productId,
            'quantity': quantity,
            'action': action
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data) {
            if (data) {
                // Находим элемент количества товара внутри строки, содержащей кнопку
                const quantityElement = button.siblings('.cart-quantity-item');
                quantityElement.text(`${data.cartCount} шт`);
                // Находим элемент суммы товара внутри строки, содержащей кнопку
                const priceElement = button.closest('tr').find('#total_price_item');
                priceElement.text(`${data.priceItem} руб`);
                $('#total_price').text(`${data.totalPrice} руб`);
                $('#total_quantity').text(`${data.totalQuantity} руб`);
            }
            console.log('Данные успешно отправлены на сервер:', data);
        },
        error: function(error) {
            console.error('Ошибка при добавлении в корзину:', error);
        }
    });
}

// При нажатии на мусорку

$('.trash_button').on('click', function() {
    const cartId = $(this).data('cartid');
    const action = $(this).data('action');
    console.log('Отправка данных на сервер: cartId =', cartId),'action', action;
    removeCart(cartId, action);
});
function removeCart(cartId, action) {
    $.ajax({
        url: 'http://127.0.0.1:8000/purchase/cart/',
        type: 'POST',
        data: {
            'cartId': cartId,
            'action': action,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data) {
            if (data.success) {
                $(`.${cartId}`).remove();
                $('#total_quantity').text(`${data.totalQuantity} руб`);
                $('#total_price').text(`${data.totalPrice} руб`);
                if (data.totalUserCart == 0) {
                $('.compleat').remove();
                $('.total').remove();
                $('.cart_container').append(emptyBlock);
                }
            }
            console.log('Данные успешно отправлены на сервер:', data);
        },
        error: function(error) {
            console.error('Ошибка при удалении корзины:', error);
        }
    });
}

// При нажатии на -

$('.decrement').on('click', function() {
    const button = $(this);
    const productId = button.data('product');
    const quantity = button.data('quantity');
    const cartId = button.data('cartid');
    const action = button.data('action');
    console.log('Отправка данных на сервер: productId =', productId, ', quantity =', quantity , 'cartId=',cartId, 'action',action);
    removeToCartWithJQuery(productId, quantity,cartId, button, action);
});
// AJAX
function removeToCartWithJQuery(productId, quantity, cartId, button, action) {
    $.ajax({
        url: 'http://127.0.0.1:8000/purchase/cart/',
        type: 'POST',
        data: {
            'product_id': productId,
            'quantity': quantity,
            'cartId': cartId,
            'action': action,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data) {
            if (data) {
                const quantityElement = button.siblings('.cart-quantity-item');
                quantityElement.text(`${data.cartCount} шт`);
                $('#total_quantity').text(`${data.totalQuantity} руб`);
                $('#total_price').text(`${data.totalPrice} руб`);
                const priceElement = button.closest('tr').find('#total_price_item');
                priceElement.text(`${data.priceItem} руб`);
                if (data.success) {
                    console.log(cartId)
                    $(`.${cartId}`).remove();
                    $('#total_quantity').text(`${data.totalQuantity} руб`);
                    $('#total_price').text(`${data.totalPrice} руб`);
                    if (data.totalUserCart == 0) {
                    $('.compleat').remove();
                    $('.total').remove();
                    $('.cart_container').append(emptyBlock);
                    }
                }
                
            }
            console.log('Данные успешно отправлены на сервер:', data);
        },
        error: function(error) {
            console.error('Ошибка при удалении товара из корзины:', error);
        }
    });
}