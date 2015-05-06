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
            if (counter >= 5) {
                htmlContent += '<li class="divider"></li> \
                    <li><a href="/notifications/" class="notification-item-more">More</a></li>';
                    break;
            }
        }
        targetDiv.append(htmlContent);
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


    $('.notifications-dropdown-container').click(function(){
        ajaxGet('/rtnotifications/', function(content){
            resetNotifications(content);
        });
    });



})(this);