$(document).ready(function(){
    $("button").click(function(){
        $("#learn").slideToggle(400);
    });
});

$(".beer").flip({
  axis: 'y',
  trigger: 'hover'
});
