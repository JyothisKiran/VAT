$(document).ready(function(){
    $(".cancel_button").click(function(){
        window.location.href ='/uploadasset/list/';
    })

    var startdate = $('#id_start_date').val().trim();
    var enddate = $('#id_end_date').val().trim();
    // if (startdate){
    //     console.log('stardate present')
    //     $("#id_end_date").attrs({'min':startdate, "placeholder" :"changed"})
    // }

    startdate.min = new Date().toISOString().split("T")[0];
    enddate.min = new Date().toISOString().split("T")[0];

    document.getElementById('id_start_date').onchange = function () {
    document.getElementById('id_end_date').setAttribute('min',  this.value);
    }

    document.getElementById('id_end_date').onchange = function () {
    document.getElementById('id_start_date').setAttribute('max',  this.value);
    }



    $(".submit_button").click(function(){
        var filename = $('#id_filename').val().trim();
        var startdate = $('#id_start_date').val().trim();
        var enddate = $('#id_end_date').val().trim();
        var fileinput = $('#id_file')[0].files[0];

        console.log("fileinput = ", fileinput)
        let data = new FormData();
        data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val())
        data.append('filename',filename)
        data.append('start_date',startdate)
        data.append('end_date',enddate)
        data.append('file',fileinput)


        console.log(filename)
        flag = true

        if (filename===""){
          $('.filenamevalidation p').show();  
          console.log('empty filename')
          flag = false
        }
        else{
            $('.filenamevalidation p').hide();
        };
        if (startdate ===""){
            $('.startdatevalidation p').show(); 
            flag = false
        }
        else{
            $('.startdatevalidation p').hide();
            console.log(startdate)
        };

        console.log("enddate = ", enddate)
        if(enddate===""){
            $('.enddatevalidation p').show(); 
            flag = false
        }
        else{
            $('.enddatevalidation p').hide();
        };
        if(fileinput==="" || fileinput === undefined){
            $('.fileinputvalidation p').show(); 
            flag = false
        }
        else{
            $('.fileinputvalidation p').hide();
        };

        if (flag == true) {
            alert("dfbd")
            $.ajax({
                url : "/uploadasset/add/",
                method :"POST",
                data : data,
                dataType : "json",
                processData: false,
                contentType: false,

                success : function(data){
                    console.log(data)
                    alert('ajax')
                    if(data.success){
                        console.log('file upload sucessful');
                        window.location.href = `/uploadasset/list/`
                    }
                    else{
                        alert("vfdvdfv");
                        console.log('file upload failed');
                        window.location.href = "/uploadasset/add_data/"
                    }
                },
                
            });
        }
        return false
        

    })
})