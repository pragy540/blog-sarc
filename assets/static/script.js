  $(document).ready(function(){
  	$("#form").hide();
    $width = $(".postfeed").width();
    $(".postfeed").css("height",$width*5/4).click(function(){
      $(this).addClass("boxshadow_removal");
      $(this).prepend("<div id='loadinganimation'></div>");
      $(this).delay(200).animate({"borderWidth":"0px"},100,"swing");
      $(this).children("#likes").fadeOut(300);
      $(this).children("#date").fadeOut(300);
      $(this).children("img").fadeOut(300);
      $(this).children("#header").delay(500).animate({top:'-70px',opacity:'0'},200,"swing");
      $(this).children("#loadinganimation").delay(700).animate({top:'30px',opacity:'0'},200,"swing");
      $(this).children("#loading").delay(600).fadeOut(0);
      var x = $(this).position();
      $("#dummy").css({"top":x.top,"left":x.left});
      var $postfeed = $(this);
      var $link = $(this).children("a")[0];
      setTimeout(function(){
        $postfeed.before("<div id='dummy'></div>");
        setTimeout(function(){$link.click();}, 900);
      }, 1000);  
      $(".postfeed").off("click");
    });
    $("#button").click(function(){
      $("#panel").css({"left":"0px"});
    });
    $("#close").click(function(){
      $("#panel").css({"left":"-100%"});
    });
    $("#search_button").click(function(){
      $("#form").slideDown("fast");
      $("#form").css("opacity","1");
      $("#form").find('input').focus();
    });
    $("#cross").click(function(){
      $('#form').slideUp("fast");
    });
    $("#dropdown").click(function(){
      $(this).children("a")[0].click();
    });
});