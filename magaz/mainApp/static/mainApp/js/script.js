document.addEventListener('DOMContentLoaded', function() {
    var authForm = document.querySelector('.auth_form');
    var darkCheckbox = document.querySelector('.dark_checkbox');

    // Пример использования JavaScript (предполагается, что у вас есть механизм для обработки ошибок)
    // При возникновении ошибки
    authForm.classList.add('errorlist');

    darkCheckbox.addEventListener('change', function() {
        var bodyElement = document.body;
        var header = document.querySelector('.header');

        // Проверка, найден ли элемент .header
        if (header) {
            // Проверка состояния чекбокса
            if (darkCheckbox.checked) {
                // Если чекбокс активен, устанавливаем темный фон
                bodyElement.style.backgroundColor = '#333';
                bodyElement.style.color = '#fff'; // Например, установите белый цвет текста
                header.style.backgroundColor = '#333';
            } else {
                // Если чекбокс неактивен, устанавливаем обычный фон
                bodyElement.style.backgroundColor = ''; // Вернуть к стандартному фону
                bodyElement.style.color = ''; // Вернуть к стандартному цвету текста
                header.style.backgroundColor = ''; // Вернуть к стандартному фону для .header
            }
        }
    });
});