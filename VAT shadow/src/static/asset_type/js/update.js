$(document).ready(function(){
    $('.cancel_button').click(function(){
        window.location.href ='/asset/list/' ;
    })

    $('.submit_button').click(function(){
        // event.preventDefault(); 
        let typename = $('#id_type_name').val().trim();
        let description = $('#id_description').val().trim();
        let asset_id = $('#asset_id').val();
        data = {
            'id':asset_id,
            'type_name':typename,
            'description':description,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
        };

        if(typename === ""){
            $('.validate p').show();
            console.log("typename empty")
        }
        else{
            $.ajax({
                url : `/asset/update/${asset_id}/`,
                method : "POST",
                data : data,
                dataType : "json",
                success: function (data){
                    if(data.success){
                        alert("Failed");
                        window.href.location = `/asset/update/${asset_id}/`;
                    }
                    else{
                        alert("succesful");
                        window.href.location = '/asset/list/';
                    }
                },
                error : function(){
                        alert("form invalid");
                        window.href.location = `/asset/update/${asset_id}/`;
                    }
                });
            }
        })
})
