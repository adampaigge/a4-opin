$(document).ready(function() {
    //hide the all of the element with class collapsible_body
    $(".collapsible_body").hide();
    //toggle the component with class collapsible_body
    $(".collapsible_head").click(function()
    {
      $(this).next(".collapsible_body").slideToggle(600);
    });

    if($(".tab-panel").length>0) {
        $(".tab-panel:not(:first-child)").hide();
    }

    $(".tab").click(function() {
        var t = $(this);
        var link = t.attr("href");
        $(".tab-panel").hide();
        $(".tab").removeClass("m-selected");
        $(this).addClass("m-selected");
        $(link).show();
        return false;
    });
});
