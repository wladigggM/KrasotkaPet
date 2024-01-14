function applyStyles(element, wasDarkmode) {
    if (wasDarkmode) {
        element.style.backgroundColor = '';
        element.style.color = '';
        element.style.borderTop = '';
        element.style.border = '';
        element.style.borderRadius = '';
        element.style.transition = '';
    } else {
        element.style.backgroundColor = '#333';
        element.style.color = 'rgb(146, 110, 129)';
        if (element.tagName.toLowerCase() === 'footer') {
            element.style.borderTop = '1px solid rgb(146, 110, 129)';
        }
        if (element.classList.contains('product')) {
            element.style.border = '1px solid rgb(146, 110, 129)';
            element.style.borderRadius = '10px';
        }
        if (element.classList.contains('header_nav')) {
            element.style.backgroundColor = 'rgb(146, 110, 129)';
        }
        // Добавляем transition ко всем изменяющимся элементам
        element.style.transition = 'all 1s ease';
    }
}

function dark_mode() {
    const body = document.body;
    const elementsToStyle = document.querySelectorAll('body, p, header, footer, .iframe, .header_nav, section h2, .product');
    const wasDarkmode = localStorage.getItem('darkmode') === 'true';

    // Инвертируем значение в локальном хранилище
    localStorage.setItem('darkmode', !wasDarkmode);
    // Инвертируем класс 'dark-mode' на body
    body.classList.toggle('dark-mode', !wasDarkmode);

    // Применяем логику для каждого элемента
    elementsToStyle.forEach(element => {
        applyStyles(element, wasDarkmode);
    });
}

document.querySelector('.theme-selector').addEventListener('click', dark_mode);
