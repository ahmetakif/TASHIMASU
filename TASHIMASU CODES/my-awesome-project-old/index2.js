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
  var PythonShell = require('python-shell');
  PythonShell.run('software.py', function (err) {
    if (err) throw err;
    console.log('finished');
  });
