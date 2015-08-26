
/* 2d */

$(document).ready(function(){
    $(".cnt").mouseenter(function(){   
      $(this).css("height","+=50px");
      $(this).children().css("font-size","+=15px");
    });
});
$(document).ready(function(){
    $(".cnt").mouseleave(function(){
      $(this).css("height","-=50px");
      $(this).children().css("font-size","-=15px");
    });
});

