
$(function(){

    $("#formation").change(function()
    {
        var formation = $("OPTION:selected", this).val();
        if (formation == '442') {
            alert($("#df").children());
            fdf = $("#df").children(".drop");
            alert(fdf);
        }
    });

    $("#id_captain").change(function()
    {
    	var pid = $(this).val();
        var img = document.createElement("img");
        img.src = "/sitemedia/images/star.gif";

    	alert(pid);
    	$("#" + pid + ".drop .selection_info").append(img);
    	
    });

	$(".block").draggable({helper:'clone'});

	$(".drop").droppable({
		accept: ".block",
		activeClass: 'droppable-active',
		hoverClass: 'droppable-hover',
		drop: drop
	});

    function drop(ev, ui) {
		var lid = ($(ui.draggable));
        var did = $(this);
        drag = lid.clone();
        drop = did.clone();
        var bench = lid.children(".selection_name").text();
        var main = did.children(".selection_name").text();

        if (confirm('Replace ' + main + ' with ' + bench + '?')) {
            colCount = $(this).siblings(".drop").size() +1;
            var benchPos = '#' + lid.children(".selection_pos").text();
            var mainPos = '#' + did.children(".selection_pos").text();
            //alert(lid.children("input").val());
            //alert(colCount);
            //alert(lid.children(".selection_pos").text());

            if (benchPos != mainPos) {
                if(benchPos == '#GK' || mainPos == '#GK') {
                    alert('Cannot substitute GK with an outfield player');
                    return;
                }
                $(mainPos).children('#' + did.attr("id")).remove();
                var posChild = $(mainPos).children(".drop").clone();
                posChild.droppable({
            		accept: ".block",
            		activeClass: 'droppable-active',
            		hoverClass: 'droppable-hover',
            		drop: drop
            	});
                $(mainPos).children().remove();

                if (colCount == 4) {
                    $(mainPos).append($(document.createElement("td")).addClass("hidden"));
                    $.each(posChild, function( intIndex, objValue ) {
                        $(mainPos).append(objValue);
                    });
                    $(mainPos).append($(document.createElement("td")).addClass("hidden"));
                } else if (colCount == 5) {
                    $.each(posChild, function( intIndex, objValue ) {
                        if(intIndex == 2) {
                            $(mainPos).append($(document.createElement("td")).addClass("hidden"));
                        }
                        $(mainPos).append(objValue);
                    });
                }

                var newPosChild = $(benchPos).children(".drop").clone();
                //alert(benchPos + ' size is ' + newPosChild.size());
                if (newPosChild.size() == 3) {
                    $(benchPos).children().remove();
                    $.each(newPosChild, function( intIndex, objValue ) {
                        if(intIndex == 2) {
                            $(benchPos).append($(document.createElement("td")).addClass("hidden"));
                        }
                        $(benchPos).append(objValue);
                    });
                    drag.removeClass().addClass('drop');
                    drag.attr('id', newPosChild.size()+1);
                    $(benchPos).append(drag);
                } else if (newPosChild.size() == 4) {

                    $(benchPos).children('.hidden').remove();
                    drag.removeClass().addClass('drop');
                    drag.attr('id', newPosChild.size()+1);

                    $(benchPos).append(drag);
                }
                lid.children().remove();
                lid.append(drop.children());
            } else {
        		var playerId = document.createElement("input")
        		playerId.type = "hidden"
        		playerId.name = "playerId"
        		playerId.value = lid.children("input").val();

                did.children().remove();
                lid.children().remove();
                did.append(drag.children());
                lid.append(drop.children());

            }
        }
	}

});