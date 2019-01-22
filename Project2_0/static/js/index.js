$(function () {
    var options = {'style': 'width:200px'};
    $('[data-toggle="popover"]').popover(options)
});

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();

    $('#ds_cokkie_info').fadeIn(3000);
    // var plzeintragen = document.GetElementById("plzeintragen");
    $("#plzeintragen").fadeIn(6000);

    $('#cookie_ok').click(function() {
      $('#ds_cokkie_info').fadeOut();
    });

    $(window).scroll(function () {

        if ($(this).scrollTop() > 150) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }

        if ($(this).scrollTop() > 200) {
            $('#search_bar3').fadeIn(600);

        } else {
            $('#search_bar3').fadeOut();
        }

      });

    // scroll body to 0px on click
    $('#back-to-top').click(function () {
        $('#back-to-top').tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

    $('#back-to-top').tooltip('show');
});
