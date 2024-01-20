        document.addEventListener("DOMContentLoaded", function () {
            var themeSelector = document.querySelector(".theme-selector");
            var linkElement = document.querySelector('link[href="{% static "mainApp/css/dark_mode.css" %}"]');

            themeSelector.addEventListener("click", function () {
                if (linkElement) {
                    linkElement.href = "{% static 'mainApp/css/style.css' %}";
                }
            });
        });