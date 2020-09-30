$(document).ready(function () {

    // Transition effect for navbar 
    $(window).scroll(function () {
        // checks if window is scrolled more than 500px, adds/removes solid class
        if ($(this).scrollTop() > 300) {
            $('#labNav').addClass('bg-dark');
            $('.top-button').show();

        } else {
            $('#labNav').removeClass('bg-dark');
            $('.top-button').hide();

        }
    });

    // Quick scroll back to top
    $('.go-top').click(function (e) {
        window.scrollTo(0, 0)
        $('#labNav').addClass('bg-semidark').removeClass('bg-dark');
        $('.top-button').hide();
    });

    // shows notification
    $('.toast').toast('show');

    // sort products in all products page
    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });

    // shows the tab at account profile
    $('#v-pills-tab a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    });

    //Tabs function not to jump on click in User-profile.html
    if (location.hash) {
        $('a[href=\'' + location.hash + '\']').tab('show');
    }
    var activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
        $('a[href="' + activeTab + '"]').tab('show');
    }

    $('body').on('click', 'a[data-toggle=\'pill\']', function (e) {
        e.preventDefault()
        var tab_name = this.getAttribute('href')
        if (history.pushState) {
            history.pushState(null, null, tab_name)
        } else {
            location.hash = tab_name
        }
        localStorage.setItem('activeTab', tab_name)

        $(this).tab('show');
        return false;
    });
    $(window).on('popstate', function () {
        var anchor = location.hash ||
            $('a[data-toggle=\'pill\']').first().attr('href');
        $('a[href=\'' + anchor + '\']').tab('show');
    });


});