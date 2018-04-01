$(document).ready(function () {
    var prev = $(window).scrollTop();
    var next = 0;
    /*Nav Bar Scrolling Change Color Effect*/
    $(document).scroll(function () {
        next = $(window).scrollTop();
        /*console.log("Scroll Occured")
        if the previous */
        /*When Scrolling Down*/
        if (next > prev) {
            $('header.navbar').css('background-color', 'white');
            $('header.navbar a').css('color', 'black');
            $('.store-name, .greeting, .log-out').css('color', 'black');

        } else {
            $("header.navbar").css('background-color', 'rgba(3, 3, 3, 0.8)');
            $('header.navbar a').css('color', '#999999');
            $('.store-name, .greeting, .log-out').css('color', '#999999');
        }
        prev = next;
    });


    //Shopping list is loaded either empty or from the localStorage
    var shopping_list = [];
    if (localStorage.getItem("shopping_list") != null) {
        shopping_list = JSON.parse(localStorage.getItem("shopping_list"));
    }
    localStorage.setItem('shopping_list', JSON.stringify(shopping_list));

    $('#cart-items').text(shopping_list.length);


    $('#Shopping-Cart').click(function () {

        window.location.href = "/ShoppingCart/Index?List=" + shopping_list;
    })



});