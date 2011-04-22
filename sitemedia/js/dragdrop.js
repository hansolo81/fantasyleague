<script language="javascript" type="text/javascript">


$(document).ready(function(){

    $(".block").draggable({helper:'clone'});

    $(".drop").droppable({
 accept: ".block",
 activeClass: 'droppable-active',
 hoverClass: 'droppable-hover',
 drop: function(ev, ui) {

 document.getElementById("display").innerHTML =  $(ui.draggable).children("li:first").text();

 var lid = ($(ui.draggable).children("li:first"));

 var removeLink = document.createElement("a");
 removeLink.innerHTML = "remove";
 removeLink.href = "#";
 removeLink.onclick = function()
 {
      $("#drop1").children().remove("#"+lid[0].id);
      $(this).remove();
 }

 $(this).append($(ui.draggable).clone().children("li:first").addClass("blocker"));
 $(this).append(removeLink);

 }
});

  });


</script>