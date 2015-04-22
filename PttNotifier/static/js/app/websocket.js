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

    $('#notification-li').click(function(){
        $('.notifications-wrapper').empty();
        var url = 'rtnotifications/';
        ajaxGet(url, function(content){
            var data = JSON.parse(content)
            console.log(data);
            var htmlContent = '';
            for(var key in data) {
                htmlContent +=
                    '<a class="content" href="' + key + '" target="_blank"> \
                        <div class="notification-item"> \
                            <h4 class="item-title">' + data[key] + '</h4> \
                            <p class="item-info">' + key + '</p> \
                        </div> \
                    </a>';
            }
            $('.notifications-wrapper').append(htmlContent);
        });
    });


})(this);