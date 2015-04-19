(function(global){
    var wsurl = 'ws://buzz3.co';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        console.log(data.notifications);
        console.log('count: ' + data.count);
        localStorage.setItem('buzz3push', data.notifications);

        $('#notifications-num').text(data.count);
        $('#notifications-num').css('display', 'block');

    });
    $('#notifications-num').click(function(){
        $(this).css('display', 'none');
    });


})(this);