var logging = require('./logger.js').logging();
var pg = require('pg');
var util = require('util');
var conString = "postgres://username:password@localhost/database";

var User = function(){
	EventEmitter.call(this);
	this.client = null;
};
util.inherits(User, EventEmitter);


User.prototype.getall = function(callback){
	pg.connect(conString, function(err, client, done) {
		if(err) {
			return console.error('error fetching client from pool', err);
		}
		client.query('SELECT * from subscription_user', function(err, result) {
		//call `done()` to release the client back to the pool
			done();

			if(err) {
		  		return console.error('error running query', err);
			}
			console.log(result.rows[0].number);
			//output: 1
			client.end();
		});
	});
};

User.prototype.getMail = function(id, callback){
	pg.connect(conString, function(err, client, done) {
		if(err) {
			return console.error('error fetching client from pool', err);
		}
		client.query('SELECT * from subscription_user where id=($1)', [id], function(err, result) {
		//call `done()` to release the client back to the pool
			done();

			if(err) {
		  		return console.error('error running query', err);
			}
			console.log(result.rows[0].number);
			//output: 1
			client.end();
		});
	});
}

module.exports = User;