var express = require('express');
var app = express();
var fs = require('fs');
var mysql = require('mysql');

var connection = mysql.createConnection({
	host : 'localhost',
	user : 'sensor',
	password : 'raspberry',
	database : 'data'
});

connection.connect();

app.get('/', function(req, res) {
	res.send('hello world!');
});

app.get('/insert', function(req, res) {

	req.query.value = Number(req.query.value);
	fs.appendFile('log.txt', JSON.stringify(req.query), function(err){
	});
	connection.query('insert into sensors set ?', req.query);	
	console.log('data receive!' + JSON.stringify(req.query));
	res.send(JSON.stringify(req.query));
});

app.get('/update', function(req, res) {
	console.log("got it");
	console.log(req.query);
	console.log(typeof req.query);
	console.log(typeof JSON.stringify(req.query));
	console.log(typeof JSON.parse(JSON.stringify(req.query)));
	console.log(typeof req.query.api_key);
	res.send('Hello World!');
});

app.listen(3000, function() {
	console.log('example app listening on port 3000');
});
