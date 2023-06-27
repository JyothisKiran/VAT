$(document).ready(function(){
    $('.cancel_button').click(function(){
        window.location.href ='/asset/list/' ;
    })

    $('.submit_button').click(function(){
        // event.preventDefault(); 
        let typename = $('#id_type_name').val().trim();
        let description = $('#id_description').val().trim();
        data = {
            'typename':typename,
            'description':description,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
        };

        if(typename === ""){
            $('.validate p').show();
            console.log("typename empty")
        }
        else{
            $.ajax({
                url : '',
                method : "POST",
                data : data,
                dataType : "json",
                success: function (data){
                    if(data.success){
                        alert("Successful");
                        window.href.location = '';
                    }
                    // else{
                    //     alert("error");
                    // }
                },
                error : function(){
                        alert("form invalid");
                    }
                });
            }
        })
})
