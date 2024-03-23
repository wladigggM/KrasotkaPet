    var selectedTheme = localStorage.getItem('selectedTheme');
    if(selectedTheme) {
        $("link[rel=stylesheet]:eq(2)").attr("href", selectedTheme);
    }

    $(".theme-selector").click(function(){
        var newTheme;
        if(selectedTheme === '/static/mainApp/css/dark_mode_now.css') {
            newTheme = '/static/mainApp/css/style.css';
        } else {
            newTheme = '/static/mainApp/css/dark_mode_now.css';
        }
        $("link[rel=stylesheet]:eq(2)").attr("href", newTheme);

        selectedTheme = newTheme;
        localStorage.setItem('selectedTheme', newTheme);
    });