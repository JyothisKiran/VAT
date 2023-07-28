$(document).ready(function(){
    $('.cancel_button').click(function(){
        window.location.href = `/company/list/`
    })


    $('.submit_button').click(function(){
    let company_name = $('#id_company_name').val().trim();
    let company_code = $('#id_company_code').val().trim();
    let contact_person = $('#id_contact_person').val().trim();
    let phone_number = $('#id_phone_number').val().trim();
    let email = $('#id_email').val().trim();

    data = {
        'company_name':company_name,
        'company_code':company_code,
        'contact_person':contact_person,
        'phone_number':phone_number,
        'email':email,
        'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
    };

    
        alert('submitted')
        console.log("code= ", company_code)
        
        console.log(company_code,company_code,contact_person,phone_number,email)
        window.location.href = `/company/list/`

        $.ajax({
            url: `/company/add/`,
            method:'POST',
            data:data,
            dataType: 'json',
            success:function(data){
                if(data.success){
                    alert('all okay')
                    window.location.href =`/company/list/`
                }
                else{
                    alert('company code already exits');
                    window.location.href=`/company/add/`
                }
            }
        });
    })

    

})