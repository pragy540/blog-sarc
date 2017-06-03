  $(document).ready(function(){
    $("#search").hide();
    $("#panel").hide();
    $width = $(".postfeed").width();
    $(".postfeed").css("height",$width*5/4);

    $("#button").click(function(){
      $("#panel").show();
    });

    $("#close").click(function(){
      $("#panel").hide();
    });

    $("#btn").children("span").click(function(){
      $("#search").show();
      $("#search").find("input").focus();
    });

    $("#cross").click(function(){
        $("#search").hide();
    });
});


/*

    */