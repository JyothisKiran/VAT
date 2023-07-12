$(document).ready(function(){
    let flag =0 ;
    $(".cancel_button").click(function() {
        window.location.href ='/asset/list/' ;
    })


    $('.submit_button').click(function(){
        let type_name = $('#id_type_name').val().trim();
        let description = $('#id_description').val().trim();
        datas = {
            'typename':type_name,
            'description':description,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
        };
        
        if (type_name === ""){
            $('.validate p').show();
            console.log("typename empty")
            // alert("kjhki,fsh");
            return false
        }

        else{
            $.ajax({
                url : '/asset/add/',
                method : 'POST',
                data : datas,
                dataType : "json",
                // fail : function(data){
                    
                // },
                success : function(data){
                    console.log("success block");
                    if(data.success){
                        console.log('success')
                        window.location.href = '/asset/list/'
                    }
                    else if(data.fail){
                        console.log('Please enter another name');
                        window.location.href = '/asset/add/'
                    }
                    else{
                        console.log("Error has occured");
                    }
                },
                error : function(){ 
                    console.log('data = ', data)
                    alert("form invalid");
                    console.log('error')
                    window.location.href  = '/user/success/'
                }
            });
        }
    })


})