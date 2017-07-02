  $(document).ready(function(){
  	$("#form").hide();

    $width = $(".postfeed").width();
    $(".postfeed").css("height",$width*5/4);

    $("#button").click(function(){
      $("#panel").css({"left":"0px"});
    });
    $("#close").click(function(){
      $("#panel").css({"left":"-100%"});
    });
    $("#search_button").click(function(){
    	$("#form").slideDown("fast");
    	$("#form").css("opacity","1");
      $("#form").autofocus();
    });
    $("#cross").click(function(){
    	$("#form").slideUp("fast");
    });
});