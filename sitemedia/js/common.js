$(function(){
    $('.viewplayer').click(function(e) {
		//e.preventDefault();
        getPlayerInfo($(this).attr("id"));
    });


    $("#id_team").change(function(){
        getPlayers($(this));
    });


    $(".block").Tooltip({
        track: true,
        delay: 0,
        fade: 250
    });

    $("#main li, .current_page_item a").corner("top");
    $(".leaguecontainer div").corner("top");

    $("#id_value").change(function(){
        getPlayers($(this));
    });



    function getPlayers(elem) {

        var position = $("div.selectedfilter").attr("id");
        var teamId = -1;
        var valueId = -1;
        //var id = elem.attr("id");
        var url ='/base/players/';
        if (elem.attr("class") == 'selectedfilter' || elem.attr("class") == 'positionfilter') {
            position = elem.attr("id") ;
            teamId = $("#id_team").val();
            if (position == '') {
                position = -1;
            }
            if (teamId == '') {
                teamId = -1;
            }
            if (valueId == '') {
                valueId = -1;
            }
        } else if (elem.attr("id") == "id_team") {
            teamId = elem.val();
            valueId = $("#id_value").val();
            if (position == '') {
                position = -1;
            }
            if (teamId == '') {
                teamId = -1;
            }
            if (valueId == '') {
                valueId = -1;
            }
        } else {
            teamId = $("#id_team").val();
            valueId = elem.val();
            if (position == '') {
                position = -1;
            }
            if (teamId == '') {
                teamId = -1;
            }
            if (valueId == '') {
                valueId = -1;
            }
        }

        var url ='/base/players/' + position + '/' + teamId + '/' + valueId;
        //alert(url);

        var table = $("table#playerfilter");
        var header = $("table#playerfilter tr.header");

        $.ajax({
            url: encodeURI(url),
            contentType: "application/javascript; charset=utf-8",
            dataType: "json",
            error: function(msg) {
                alert('error' + msg);
            },
            success: function(msg) {
                table.children().remove();
                table.append(header);
                jQuery.each(msg, function(i, val) {
                    var template = [{
                        tagName: 'tr',
                        className: 'playerlist',
                        childNodes : []
                    }];
                    var content = template[0].childNodes;
                    content.push({
                        tagName : 'td',
                        childNodes : [{
                        tagName : 'a',
                        id: ''+val.pk,
                        href: "#",
                        className: 'viewplayer',
                        onclick: function(){
                            getPlayerInfo(''+val.pk);
                        },
                        innerHTML: '<img src="/sitemedia/images/info-icon.png">'
                        }]
                        },
                        {
                          tagName : 'td',
                          title: 'Drag Me to the Pitch!',
                          id: ''+val.pk,
                          className: 'block',
                          childNodes : [{
                                tagName : 'div',
                                innerHTML: val.fields['firstname']
                            },
                            {
                                tagName : 'div',
                                innerHTML: val.fields['lastname']
                          }]
                        },
                        {
                          tagName : 'td',
                          className: 'position',
                          childNodes : [{
                                tagName : 'div',
                                innerHTML: val.fields['position'].fields['code']
                            }]
                        },
                        {
                          tagName : 'td',
                          className: 'value',
                          childNodes : [{
                                tagName : 'div',
                                innerHTML: val.fields['value']
                            }]
                        },
                        {
                          tagName : 'td',
                          className: 'points',
                          childNodes : [{
                                tagName : 'div',
                                innerHTML: ''+val.extras['total_points']
                            }]
                        },
                        {
                          tagName : 'td',
                          className: 'team',
                          id: val.extras['current_team_code']
                        }
                    );
                    table.appendDom(template);
	                $(".block").draggable({helper:'clone'});
                    $(".block").Tooltip({
                        track: true,
                        delay: 0,
                        fade: 250
                    });
                });
            }
        });

    }

    $(".filtercontainer div").click(function(){
        var prevselected = $("div.selectedfilter");
        prevselected.removeClass().addClass("positionfilter");
        $(this).removeClass().addClass("selectedfilter");
        getPlayers($(this));
    });

    function getPlayerInfo(id) {
        $.ajax({
            url: encodeURI('/base/player_details/' + id),
            contentType: "application/javascript; charset=utf-8",
            dataType: "json",
            error: function(msg) {
                alert(msg);
            },
            success: function(msg) {
                //alert(msg);
                $('div#playerBio').children().remove();
                var template = [{
                    tagName: 'div',
                    className: 'playerBioHeader',
                    innerHTML : msg[0].extras['__unicode__']
                },
                {
                    tagName: 'div',
                    className: 'playerBioPic',
                    innerHTML: '<img src="/sitemedia/images/players/'+ msg[0].pk + '.jpg">'
                },
                {
                    tagName: 'div',
                    className: 'playerBioContent',
                    childNodes : []
                }];
                var content = template[2].childNodes;
                content.push({
                  tagName : 'table',
                  childNodes : [{
                    tagName : 'tbody',  // tbody is needed for Internet Exlorer
                    childNodes : []
                  }]
                })

               addRow(content, 'Position', msg[0].fields['position'].fields['code']);
               addRow(content, 'Team', msg[0].extras['current_team']);
               addRow(content, 'Next Opponent', 'Johor');
               addRow(content, 'Total Pts', msg[0].extras['total_points']);

               $('div#playerBio').appendDom(template);
            }
        });

        //$.blockUI({ message: $('#playerBio') });
        $('div#playerBio').modal({
            onOpen: function (dialog) {
        	dialog.overlay.fadeIn('slow', function () {
        		dialog.container.slideDown('slow', function () {
        			dialog.data.fadeIn('slow');
        		});
        	});
            },
            onClose: function (dialog) {
            	dialog.data.fadeOut('slow', function () {
            		dialog.container.slideUp('slow', function () {
            			dialog.overlay.fadeOut('slow', function () {
            				$.modal.close(); // must call this!
            			});
            		});
            	});
            }});
        //setTimeout($.unblockUI, 2000);
    }

    function addRow(content, statname, msg) {
        var row = content[0].childNodes;
        row.push({
            tagName : 'tr',
            childNodes : [{
                tagName : 'th',
                innerHTML : statname
            },
            {
                tagName: 'td',
                innerHTML : msg
            }]
        });
    }
});

$(document).ready(function(){

    $('.gwinfo').Tooltip({
        track: true,
        delay: 0,
        showBody: "-",
        fade: 250
    });


});