(function(global){
    var wsurl = 'ws://buzz3.co';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        console.log(data.notifications);
        var notifications_pool = localStorage.getItem('buzz3push');

        if(!notifications_pool){
            notifications_pool = [];
        }
        notifications_pool.push(data.notifications);
        localStorage.setItem('buzz3push', notifications_pool);
        var pushCount = notifications_pool.length;

        $('#notifications-num').text(pushCount);
        $('#notifications-num').css('display', 'block');

    });
    $('#notifications-num').click(function(){
        $(this).css('display', 'none');
    });


})(this);