(function(global){
    var wsurl = 'ws://buzz3.co';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        console.log('count: ' + data.count);
        localStorage.setItem('buzz3push', data.count);
        $('.notifications-dropdown-container').text(data.count);
    });

    var onAckNotification = function(){
        $('.notification-item').click(function(){
            var url = $(this).attr('href');
            var title = $(this)[0].innerText;
            var postBody = { 'url': url, 'title': title }
            ajaxPost('/rtnotifications/update/', postBody, function(content){
                console.log('got feedback');
                resetNotifications(content);
                $('.notifications-dropdown-container').text(
                    Object.keys(JSON.parse(content)).length);
            });
        });
    };

    var resetNotifications = function(content){
        var targetDiv = $('#notifications-binding');
        targetDiv.empty();
        var data = JSON.parse(content)
        console.log(data);
        var htmlContent = '';
        var counter = 0;
        for(var key in data) {
            htmlContent += '<li><a class="notification-item" href="' + key + '" target="_blank">' + data[key] + '</a></li>';
            counter++;
            if (counter >= 10) {
                break;
            }
        }
        htmlContent += '<li class="divider"></li> \
                    <li class="dropdown-fifty"><a href="/notifications/" class="notification-item-more">檢視全部</a></li> \
                    <li class="dropdown-fifty"><a href="/notifications/delete/" class="notification-item-more">清除全部</a></li>';
        targetDiv.append(htmlContent);
        onAckNotification();
    };

    onAckNotification();

    $('.notification_list_row').click(function(){
        $(this).remove();
    });


    $('.notifications-dropdown-container').click(function(){
        ajaxGet('/rtnotifications/', function(content){
            resetNotifications(content);
        });
    });



})(this);