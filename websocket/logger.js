var winston = require('winston');
	winston.add(winston.transports.File, { filename: 'redis_nodejs.log' });
exports.logging = function(){
	// winston.remove(winston.transports.Console);
	return winston;
};

