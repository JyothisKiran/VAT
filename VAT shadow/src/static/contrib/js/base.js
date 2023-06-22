$(document).ready(function(){
  $('.collapse-content').show();
  $('.right_arrow').hide();
  $("#collapse_btn").click(function () {
    // Toggle visibility of the collapse content
    if($('.collapse-content').css({'display':'block'})){
      console.log('expanded');
      $('.right_arrow').show();
      $('.left_arrow').hide();
      $('.navbarContents').css({'width':'87.7px'})
      $('.collapse-content').hide();
      $('.sidebar').css({'width':'56px', "transition": "0.7s" });
      $('li').css({'width':'38px'})
      $("#collapse_btn").css({'margin-left':'31px',"transition": "0.7s" });
    }
    // if ($('.collapse-content').css({'display':'none'})) {
    //   console.log('collapsed');
    //   $('.collapse-content').show();
    // }
    else{
      $('.collapse-content').show();
    };
  });
       
})