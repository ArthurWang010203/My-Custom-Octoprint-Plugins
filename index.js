var express = require('express');
var app = express();
var fs = require('fs');
const port = 3000
const router = express.Router();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true });

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
	fs.readFile('/home/pi/status.txt', 'utf8', function(err, data) {
		if (err) throw err;
		const lines = data.split(/\r?\n/);
		var toPrint = lines[0]+": " + lines[1] //data[0]+": " + data[1]+" updated";
		var startTime = lines[2];
		res.render('/home/pi/statusPage/index.ejs', {
			printThis: toPrint,
			connectIp: "10.0.0.115", 
			started: startTime //lines[2] //"10.0.0.115"
		});
	});
});
app.post('/addCart', function (req, res) {
	fileToSend = req.body.zeFile;
});

app.use('/', router);
console.log('Operating on Port: '+port);
app.listen(process.env.port || port);
