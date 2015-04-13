(function(global){
    var wsurl = 'ws://buzz3.co:8000';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        $('#notifications-num').text(data.count);
        $('#notifications-num').css('display', 'block');
    });



})(this);