

// $(document).ready(function() {
//     $(".pass_togg").click(function() {
//         var passwordInput = $("#id_password");
//         var passwordVisibleImg = $("#.pass_toggle_show");
//         // $(".pass_toggle_hide").toggle();
//         // $(".pass_toggle_show").toggle();

//         if (passwordInput.attr("type") === "password") {
//             passwordInput.attr("type", "text");
//             passwordVisibleImg.attr("src", "{% static 'users/images/Hide.svg' %}");
//         } else {
//             passwordInput.attr("type", "password");
//             passwordVisibleImg.attr("src", "{% static 'users/images/Show.svg' %}");
//         }
//     });
// });



$(document).ready(function() {
    // Handle form submission
    $("#forgot_pw a").click(function(){
        window.location.href = `/user/forgotpw/`
    })
    $("form").submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        var username = $("#id_username").val();
        var password = $("#id_password").val();

        // AJAX request to validate the login credentials
        $.ajax({
            url: "/user/login/", // Replace with the actual URL or path to your server-side validation view
            method: "POST",
            data: { username: username, password: password ,csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()},
            dataType: "json",
            success: function(response) {
                console.log
                if (response.success) {
                    // Redirect to the home page or perform any other desired action
                    window.location.href = "/user/success/";
                } else {
                    // Display error message or perform any other desired action
                    window.alert("Invalid credentials");
                }
            },
            error: function() {
                // Handle the error scenario
                if (username === '' && password === ''){
                    $('.validate_cred p').show();
                }
                else{
                    $('.validate_cred p').hide();
                    $('.validate').show();
                }
                
            }
        });
    });

    // Toggle password visibility
    $(".pass_togg").click(function() {
        var passwordInput = $("#id_password");
        var passwordToggler = $(".pass_togg");
        var passwordVisibleImg = $(".pass_toggle_show");
        var passwordHideImg = $(".pass_toggle_hide");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            passwordVisibleImg.show();
            passwordHideImg.hide();
        } else {
            passwordInput.attr("type", "password");
            passwordVisibleImg.hide();
            passwordHideImg.show();
        }
    });
});

