var Blynk = require('blynk-library'),
    AUTH = '9f0d81c9f36b4247af7baf5984b779ab',
    blynk = new Blynk.Blynk(AUTH),
    v0 = new blynk.VirtualPin(0);

v0.on('write', function(param) {
  var x = param[0];
  tasker(x);
});

function tasker(x) {
  var data = parseInt(x),
      fs = require('fs'),
      data = JSON.stringify(data);
  fs.writeFile('word.json', data, finished);
  function finished(err) {
    console.log('OK');
  }
  var spawn = require('child_process').spawn,
      py    = spawn('python', ['software.py']);
