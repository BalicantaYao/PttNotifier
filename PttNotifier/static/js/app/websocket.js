(function(global){
	var wsurl = 'ws://buzz3.co:8000';
  var socket = io.connect(wsurl);

  socket.on('date', function(data) {
    $('#wstest').text(data.date);
  });

})(this);