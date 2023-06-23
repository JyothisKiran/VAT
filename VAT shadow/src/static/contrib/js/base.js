$(document).ready(function(){
  $('.collapse-content').show();
  $('.right_arrow').hide();
  var flag = 0;
  var flag_btn =0;
  $("#collapse_btn").click(function () {
    // Toggle visibility of the collapse content
    if(flag === 0){
      console.log('expanded');
      flag = 1;
      // $('.right_arrow').show();
      $('.left_arrow').css({'transform':'rotateZ(180deg)','margin-top':'-9px'});
      $('.collapse-content').css({'display':'none'});
      $('.sidebar').css({'width':'56px', "transition": "0.7s" });
      $('.sidebar_list').css({'width':'38px'})
      $("#collapse_btn").css({'margin-left':'31px',"transition": "0.7s" });
    }
    // else if ($('.collapse-content').css({'display':'none'})) {
    //   console.log('collapsed');
    //   $('.collapse-content').show();
    // }
    else{
      // $('.right_arrow').hide();
      $('.left_arrow').css({'transform':'rotateZ(360deg)','margin-top':'0px'});
      $('.collapse-content').show();
      $('.sidebar').css({'width':'250px', 'transition': '0.7s' });
      $('.sidebar_list').css({'width':'230px'});
      $("#collapse_btn").css({'margin-left':'225px','transition': '0.7s' });
      flag =0;
    };
  });

  $('.systemsettings_btn').click(function(){
    if(flag_btn === 0){
      $('.acordion-list').show();
      $('.acordion-list').css({'transition':'0.7s'});
      // $('.dropdown_arrow').css({'transform':'rotate(180deg)'});
      $('.dropdown_arrow').hide();
      $('.dropdown_arrowup').show();
      flag_btn=1;
    }
    else{
      flag_btn=0;
      $('.acordion-list').hide();
      $('.acordion-list').css({'transition':'0.7s'});
      // $('.dropdown_arrow').css({'transform':'rotate(360deg)'});
      $('.dropdown_arrow').show();
      $('.dropdown_arrowup').hide();
    }
  })
       
})