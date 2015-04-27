(function(global){
    var wsurl = 'ws://buzz3.co';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        console.log('count: ' + data.count);
        localStorage.setItem('buzz3push', data.count);
        $('#notification-a').text(data.count);
    });

    var resetNotifications = function(content){
        var targetDiv = $('.notifications-wrapper');
        targetDiv.empty();
        var data = JSON.parse(content)
        console.log(data);
        var htmlContent = '';
        for(var key in data) {
            htmlContent +=
                '<a class="notification-content-block" href="' + key + '" target="_blank"> \
                    <div class="notification-item"> \
                        <h4 class="item-title">' + data[key] + '</h4> \
                        <p class="item-info">' + key + '</p> \
                    </div> \
                </a>';
        }
        targetDiv.append(htmlContent);
    };

    $('#notification-li').click(function(){
        ajaxGet('/rtnotifications/', function(content){
            resetNotifications(content);
        });
    });
    $('.notification-content-block').click(function(){
        var url = $(this).find('.item-title').text;
        var title = $(this).find('.item-info').text;
        var postBody = { 'url': url, 'title': title }
        ajaxPost('/rtnotifications/update', postBody, function(content){
            resetNotifications(content);
        });
    });


})(this);