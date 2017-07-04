  $(document).ready(function(){
  	$("#form").hide();
    $("#input").blur();
    $width = $(".postfeed").width();
    $(".postfeed").css("height",$width*5/4);

    $("#button").click(function(){
      $("#panel").css({"left":"0px"});
    });
    $("#close").click(function(){
      $("#panel").css({"left":"-100%"});
    });
});