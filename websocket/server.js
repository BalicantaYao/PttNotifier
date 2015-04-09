var http = require('http');
var url = require('url');
var fs = require('fs');
var io = require('socket.io');
var logging = require('./logger.js').logging();

var server = http.createServer(function(request, response) {
    console.log('Connection');
    var path = url.parse(request.url).pathname;

    switch (path) {
        case '/':
            response.writeHead(200, {
                'Content-Type': 'text/html'
            });
            response.write('Hello, World.');
            response.end();
            break;
        default:
            response.writeHead(404);
            response.write("opps this doesn't exist - 404");
            response.end();
            break;
    }
});

server.listen(8000);

var serv_io = io.listen(server);
var cookie_reader = require('cookie');

serv_io.set('authorization', function(data, accept){
    if(data.headers.cookie){
        data.cookie = cookie_reader.parse(data.headers.cookie);
        logging.info('user cookie: ' + data.cookie);
        // logging.info(data.cookie.sessionid);
        var redisClient = require('./redisClient.js');
        var redis = new redisClient();
        redis.connect(6379, '127.0.0.1');
        redis.select(1, function(){
            if (!err) {
                redis.get(data.cookie.sessionid, function(err, res){
                    if (!err) {
                        logging.info(res);
                    }
                    redis.close();
                });
            }
        });

        return accept(null, true);
    }
    return accept('error', false);
});

serv_io.sockets.on('connection', function(socket) {
    console.log('socket.id: ' + socket.id);

    setInterval(function() {
        socket.emit('date', {
            'date': new Date()
        });
    }, 1000);

    socket.on('disconnect', function() {
        console.log('Got disconnect! id: ' + socket.id);
    });
});