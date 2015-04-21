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
        var url = 'rtnotifications/';
        ajaxGet(url, function(content){
            alert(content);
        });
    });

})(this);