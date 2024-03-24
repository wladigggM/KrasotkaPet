$(document).ready(function() {
    url = window.location.href;
    // Проверяем текущий URL страницы
    if (url !== 'http://127.0.0.1:8000/purchase/cart/' && url !== 'http://127.0.0.1:8000/users/account/') {
    $('.add-to-cart').on('click', function() {
    const productId = $(this).data('product');
    const quantity = $(this).data('quantity');
    const path = $(this).data('path');
    const size = $('#size').val();
    console.log('Отправка данных на сервер: productId =', productId, ', quantity =', quantity,'path=', path , 'size = ', size);
    addToCartWithJQuery(productId, quantity, path, size);
});

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
function addToCartWithJQuery(productId, quantity, path, size) {
    $.ajax({
        url: path,
        type: 'POST',
        data: {
            'product_id': productId,
            'quantity': quantity,
            'size': size,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data) {
            if (data.cartCount) {
                $('#cart-count').text(`${data.cartCount}`);
            }
            $('#success-message').text('Товар успешно добавлен в корзину.').show();
            console.log('Данные успешно отправлены на сервер:', data);

            // Скрывает сообщение через 5 секунд
            setTimeout(function() {
                $('#success-message').fadeOut();
            }, 2000);
        },
        error: function(error) {
            console.error('Ошибка при добавлении в корзину:', error);
        }
    });
}
    } else if (
    url === 'http://127.0.0.1:8000/purchase/cart/' ||
    url === 'http://127.0.0.1:8000/users/account/'
    ) {
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
    const path = $(this).data('path');
    const size = $(this).data('size');
    console.log('Отправка данных на сервер: productId =', productId, ', quantity =', quantity,'action', action, 'path=', path, 'size=', size);
    addToCartWithJQuery(productId, quantity, button, action, path, size);
});
// AJAX
function addToCartWithJQuery(productId, quantity, button, action, path, size) {
    $.ajax({
        url: path,
        type: 'POST',
        data: {
            'product_id': productId,
            'quantity': quantity,
            'action': action,
            'size': size,
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
    const productId = $(this).data('product');
    const action = $(this).data('action');
    const path = $(this).data('path');
    const size = $(this).data('size');
    console.log('Отправка данных на сервер: cartId =', cartId,'action=', action, 'path', path, 'productId', productId, 'size=', size);
    removeCart(cartId, action, path, productId, size);
});
function removeCart(cartId, action, path, productId, size) {
    $.ajax({
        url: path,
        type: 'POST',
        data: {
            'cartId': cartId,
            'action': action,
            'size': size,
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
                $('.cart_container table:first').after(emptyBlock);
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
    const path = button.data('path');
    const size = $(this).data('size');
    console.log('Отправка данных на сервер: productId =', productId, ', quantity =', quantity , 'cartId=',cartId, 'action',action, 'path=', path, 'size=', size);
    removeToCartWithJQuery(productId, quantity,cartId, button, action, path, size);
});
// AJAX
function removeToCartWithJQuery(productId, quantity, cartId, button, action, path, size) {
    $.ajax({
        url: path,
        type: 'POST',
        data: {
            'product_id': productId,
            'quantity': quantity,
            'cartId': cartId,
            'action': action,
            'size': size,
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

$('.clear_order_button').on('click', function() {

    const path = $(this).data('path');
    const orderId = $(this).data('order');
    console.log(orderId)
    const action = $(this).data('action');
    console.log('Отправка данных на сервер:', 'orderId=', orderId, 'action= ', action, 'path=', path );

    removeOrder(orderId, action, path);

});

function removeOrder(orderId, action, path) {
    $.ajax({
        url: path,
        type: 'POST',
        data: {
            'orderId': orderId,
            'action': action,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data) {
            if (data) {
                $('#' + orderId).remove();
            }
            console.log('Данные успешно отправлены на сервер:', data);
        },
        error: function(error) {
            console.error('Ошибка при удалении корзины:', error);
        }
    });
}

    }
});