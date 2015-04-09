
var logging = require('./logger.js').logging();
var redis = require('redis');
var util = require('util');
var EventEmitter = require('events').EventEmitter;

// var RedisClientUtil = function(){
function RedisClientUtil(){
	EventEmitter.call(this);
	this.client = null;
}
util.inherits(RedisClientUtil, EventEmitter);

RedisClientUtil.prototype.connect = function(port, redisServer){
	var self = this;
	self.client = redis.createClient(port, redisServer);
	self.client.on('error', function(err){
		logging.error('[RedisClientUtilError]' + err);
		try{
			self.client.end();
		}
		catch (e){
			logging.error('[RedisClientUtilInitEx]' + e);
			return new Error(e);
		}
		// return new Error(err);
		self.emit('error', err);
	});
};

RedisClientUtil.prototype.hgetall = function(callback){
	var self = this;
	var allNotificationsByUser = {};
	var checkFinishAry = [];
	self.client.keys('*', function(err, keys){
		if (!err) {
			keys.forEach(function(eachKey){
			 	allNotificationsByUser[eachKey] = [];
				self.client.hgetall(eachKey, function(err, hashset){
					if (!err) {
						var userNotifications = [];
						for (var hkey in hashset) {
							userNotifications.push({ 't': hashset[hkey], 'u': hkey });
						}
						allNotificationsByUser[eachKey] = userNotifications;
					}
					else{
						//key not found
						logging.error('[HGETALLERROR KEY: ' + eachKey + ']' + err);
						// callback && callback.call(self, err);
					}
					// self.client.quit();

					checkFinishAry.push(1);
					if (checkFinishAry.length == keys.length) {
						callback && callback.call(self, err, allNotificationsByUser);
					}
				});
			 });
		}
		else{
			logging.error('[KEYSERROR]' + err);
			// return new Error(err);
			self.emit('error', err);
		}
		// self.client.quit();
	});
};

RedisClientUtil.prototype.hdel = function(mainKey, hashKey){
	var self = this;
	self.client.hdel(mainKey, hashKey);
};

RedisClientUtil.prototype.getall = function(callback){
	var self = this;
	var allNotificationsByUser = {};
	var checkFinishAry = [];
	self.client.keys('*', function(err, keys){
		if (!err) {
			keys.forEach(function(eachKey){
			 	allNotificationsByUser[eachKey] = [];
				self.client.get(eachKey, function(err, result){
					if (!err) {
						allNotificationsByUser[eachKey] = result;
					}
					else{
						//key not found
						logging.error('[HGETALLERROR KEY: ' + eachKey + ']' + err);
						// callback && callback.call(self, err);
					}
					// self.client.quit();

					checkFinishAry.push(1);
					if (checkFinishAry.length == keys.length) {
						callback && callback.call(self, err, allNotificationsByUser);
					}
				});
			 });
		}
		else{
			logging.error('[KEYSERROR]' + err);
			// return new Error(err);
			self.emit('error', err);
		}
		// self.client.quit();
	});
};
RedisClientUtil.prototype.get = function(key, callback){
	var self = this;
	self.client.get(key, callback);
};

RedisClientUtil.prototype.select = function(db, callback){
	var self = this;
	self.client.select(db, callback);
};

RedisClientUtil.prototype.close = function(){
	var self = this;
	if (self.client) {
		try{
			self.client.end();
		}
		catch (e){
			logging.error('[RedisClientUtilCloseEx]' + e);
			emit('error', e);
			// throw (err);
		}
	}
};

module.exports = RedisClientUtil;

