$(document).ready(function(){
    let typename = $('#id_type_name').val().trim();
    let description = $('#id_description').val().trim();
    $('.submit_button').click(function(){
        if (typename === "" ){
            $('.validate p').show();
        }
        
    })
})