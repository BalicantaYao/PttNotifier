var logging = require('./logger.js').logging();

process.on('uncaughtException', function(err) {
    logging.error('[uncaughtException]', err);
});
var domain = require('domain').create();
domain.on('error', function(err){
	logging.error('[DomainError]' + err);
});

domain.run(function(){
	var redisClient = require('./redisClient.js');
	var redis = new redisClient();

	redis.connect(6379, '127.0.0.1');
	redis.hgetall(function(err, res){
		if (!err) {
			console.log(res);
			redis.close();
		}
		else{
			console.log('err');
		}
	});

});
