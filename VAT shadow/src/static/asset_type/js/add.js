$(document).ready(function(){
    let flag =0 ;
    $(".cancel_button").click(function() {
        window.location.href ='/asset/list/' ;
    })


    $('.submit_button').click(function(){
        let type_name = $('#id_type_name').val().trim();
        let description = $('#id_description').val().trim();
        data = {
            'typename':type_name,
            'description':description,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
        };

        if (type_name === ""){
            $('.validate p').show();
            console.log("typename empty")
        }

        else{
            $.ajax({
                url : '/asset/add/',
                method : 'POST',
                data : data,
                dataType : "json",
                success : function(data){
                    if(data.success){
                        alert("Successful");
                        window.location.href = '/asset/list/'
                    }
                    else{
                        alert("Error has occured");
                    }
                },
                error : function(){ 
                    alert("form invalid");
                    window.location.href  = '/asset/list/'
                }
            });
        }
    })


})