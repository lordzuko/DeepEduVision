$(document).ready(function() {

    $('.menu .item').tab()
    }
                   
                   
);
    

function modal(){
    $('.ui.modal')
        .modal({
            blurring: true
        })
        .modal('show');               
}

function rate() {
    $('.ui.star .rating')
        .rating({
            initialRating: 5,
            maxRating: 5
        });
}