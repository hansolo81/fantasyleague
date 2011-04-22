

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

	$("a.remove").click(function(){
		//$(".drop").children().remove("#"+$(this).attr("id"))
		$(this).siblings().remove();
        var img = document.createElement("img");
        img.src = '/sitemedia/images/shirta_0.gif'
        $(this).parent().append(img);
		$(this).remove();
		calculateMoney();
	});
	
	$("#target").submit(function()
		{
			if (calculateMoney()<0) {
				alert('You have negative balance in Bank.\nYou must have a positive balance to proceed.');
				return false;
			} else {
				return true;
			}
		}		
	);


	$(".block").draggable({helper:'clone'});

	$(".drop").droppable({
		accept: ".block",
		activeClass: 'droppable-active',
		hoverClass: 'droppable-hover',
		drop: function(ev, ui) {
            if ($(this).attr('id') == 'display' || confirm('Replace?')) {
            	calculateMoney();
    			var lid = ($(ui.draggable));
                var team = lid.siblings(".team").attr('id');
                var img = document.createElement("img");
                img.src = '/sitemedia/images/shirts/' + team + '.gif'

                //player name
                var playername = lid.clone().children().addClass("selection_name");
                //playername.children().remove("div");

                // remove link
    			var removeLink = document.createElement("a");
    			removeLink.innerHTML = '<img src="/sitemedia/images/delete-icon.png">';
    			removeLink.href = "#";
                removeLink.className = 'remove';
                removeLink.id = lid.attr("id");
    			removeLink.onclick = function()
    			{
            		$(this).siblings().remove();
                    var img = document.createElement("img");
                    img.src = '/sitemedia/images/shirta_0.gif'
                    $(this).parent().append(img);
                    $(this).parent().attr('id', 'display')
            		$(this).remove();
                    calculateMoney();
    			}

                // info link
    			var infoLink = document.createElement("a");
    			infoLink.innerHTML = '<img src="/sitemedia/images/info-icon.png">';
    			infoLink.href = "#";
                infoLink.className = "viewplayer";
                infoLink.id = lid.attr("id");


                // hidden player id
    			$(this).children().remove();
    			var playerId = document.createElement("input")
    			playerId.type = "hidden"
    			playerId.name = "playerId"
    			playerId.value = lid.attr("id");


                //$(this).innerHTML = '';
                $(this).attr('id', lid.attr("id"))
    			$(this).append(img);
    			$(this).append(document.createElement("br"));
    			$(this).append(removeLink);
    			$(this).append(infoLink);
    			$(this).append(playername);
    			$(this).append(lid.siblings(".value").children().clone().addClass("selection_val"));
    			$(this).append(playerId);
            	calculateMoney();
            }
		}
	});
	
	
	function calculateMoney() {
		var activecolor = '#00FF00';
		var passivecolor = '#FF0000';
		var player_val = $(".selection_val");
		var total = 0;
		var money_left = 0;

        jQuery.each(player_val, function(i, val) {
        	total+= Number(val.innerHTML);
        });
        money_left = (100 - total).toFixed(1);
        
        $(".bank").text(money_left);
        
        if (money_left >= 0) {
        	$(".bank").css('color', activecolor);
        } else {
        	$(".bank").css('color', passivecolor);
        }
        
        return money_left;  
		
	}
	

    calculateMoney();
});

