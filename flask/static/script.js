$( document ).ready(function() {
    $('nav').removeClass('bg-light');
    $('nav').addClass('bg-dark');
    $('.side-bar').css({
        'background-color': '#1c1c1c'
    })
    $('body').css({
        'background-color': '#121212',
        'color': '#EBEBEB'
    })
    $('nav').css({
        'box-shadow': 'none'
    })
    $('.dropdown-menu').css({
        'background-color': '#242424',
    })
    $('.dropdown-menu a').css({
        'color': '#BBB'
    })
    $('.form-control').css({
        'background-color': '#121212'
    })
    $('.logo-light').hide();
    $('.logo-dark').show();
    if ($('.hidden').css('display') == 'inline-block') {
        $('.hidden').css({
            'display': 'none'
        })
        $('.width-container').css({
            'width': '70%',
            'transform': 'translateX(-34%)'
        })
        $('.video-card').css({
            'width': '24.2%'
        });
        $('.side-bar').css({
            'display': 'block'
        })
    } else {
        $('.side-bar').css({
            'display': 'none'
        })
        $('.hidden').css({
            'display': 'inline-block'
        })
        $('.width-container').css({
            'width': '95%',
            'transform': 'translateX(-50%)'
        })
        $('.video-card').css({
            'width': '16.3%'
        })
    }

});

$('.bar').click(function () {
    //   hide them
    //window.location.href='index.html';
    /*if ($('.hidden').css('display') == 'inline-block') {
        $('.hidden').css({
            'display': 'none'
        })
        $('.width-container').css({
            'width': '70%',
            'transform': 'translateX(-34%)'
        })
        $('.video-card').css({
            'width': '24.2%'
        });
        $('.side-bar').css({
            'display': 'block'
        })
    } else {
        $('.side-bar').css({
            'display': 'none'
        })
        $('.hidden').css({
            'display': 'inline-block'
        })
        $('.width-container').css({
            'width': '95%',
            'transform': 'translateX(-50%)'
        })
        $('.video-card').css({
            'width': '16.3%'
        })
    }*/
});

//theme

$('.logo-light').click(function () {
    $('nav').removeClass('bg-light');
    $('nav').addClass('bg-dark');
    $('.side-bar').css({
        'background-color': '#1c1c1c'
    })
    $('body').css({
        'background-color': '#121212',
        'color': '#EBEBEB'
    })
    $('nav').css({
        'box-shadow': 'none'
    })
    $('.dropdown-menu').css({
        'background-color': '#242424',
    })
    $('.dropdown-menu a').css({
        'color': '#BBB'
    })
    $('.form-control').css({
        'background-color': '#121212'
    })
    $('.logo-light').hide();
    $('.logo-dark').show();
})
$('.logo-dark').click(function () {
    window.location.href='index.html';
    /*
    $('nav').removeClass('bg-dark');
    $('nav').addClass('bg-light');
    $('.side-bar').css({
        'background-color': '#f5f5f5'
    })
    $('body').css({
        'background-color': '#fff',
        'color': '#212529'
    })
    $('nav').css({
        'box-shadow': '1px 1px 5px #dddddd'
    })
    $('.dropdown-menu').css({
        'background-color': '#fff',
    })
    $('.dropdown-menu a').css({
        'color': '#212529'
    })
    $('.form-control').css({
        'background-color': '#fff'
    })
    $('.logo-light').show();
    $('.logo-dark').hide();
    */
})



