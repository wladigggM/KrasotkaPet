const themeSelector = document.querySelector('.theme-selector');
const linkElement = document.querySelector('link[rel="stylesheet"]');
const themeButton = document.querySelector('.theme-selector');

// Функция для установки стилей в зависимости от значения в localStorage
function setThemeFromLocalStorage() {
    const savedTheme = localStorage.getItem('selectedTheme');
    if (savedTheme) {
        linkElement.href = savedTheme;
    }
}

// Функция для обновления стилей и сохранения в localStorage
function updateAndSaveTheme() {
    if (linkElement.href.includes('/static/mainApp/css/style.css')) {
        themeButton.value = '\u{1F31A}';
        linkElement.href = '/static/mainApp/css/dark_mode.css';
        localStorage.setItem('selectedTheme', '/static/mainApp/css/dark_mode.css');
    } else {
        themeButton.value = '\u{1F31D}';
        linkElement.href = '/static/mainApp/css/style.css';
        localStorage.setItem('selectedTheme', '/static/mainApp/css/style.css');
    }
}

// Обработчик клика по селектору темы
function themeSelectorClickHandler() {
    themeSelector.addEventListener('click', function() {
        updateAndSaveTheme();
    });
}

// Вызов функции для установки стилей при загрузке страницы
setThemeFromLocalStorage();

// Вызов функции для обработки клика по селектору темы
themeSelectorClickHandler();


//
//
//
//
//
//function dark_in_light(){
//    document.addEventListener("DOMContentLoaded", function () {
//        var themeSelector = document.querySelector(".theme-selector");
//        var linkElement = document.querySelector('link[href*="dark_mode.css"]');
//
//        themeSelector.addEventListener("click", function () {
//            if (linkElement) {
//                linkElement.href = "/static/mainApp/css/style.css";
//            }
//        });
//    });
//
//}
//
//
//
//
//
//function light_in_dark(){
//    document.addEventListener("DOMContentLoaded", function () {
//        var themeSelector = document.querySelector(".theme-selector");
//        var linkElement = document.querySelector('link[href*="style.css"]');
//
//        themeSelector.addEventListener("click", function () {
//            if (linkElement) {
//                linkElement.href = "/static/mainApp/css/dark_mode.css";
//            }
//        });
//    });
//
//}