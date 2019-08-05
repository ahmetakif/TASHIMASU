var Blynk = require('blynk-library'),
    spawn = require('child_process').spawn,
    py    = spawn('python', ['compute_input.py']),
    AUTH = '9f0d81c9f36b4247af7baf5984b779ab',
    blynk = new Blynk.Blynk(AUTH),
    v0 = new blynk.VirtualPin(0),
    data = [1,2,3,4,5,6,7,8,9],
    dataString = '';

v0.on('write', function(param) {
  py.stdout.on('data', function(data){
  dataString += data.toString();
  });
  py.stdout.on('end', function(){
  console.log('Sum of numbers=',dataString);
  });
  py.stdin.write(JSON.stringify(data));
  py.stdin.end();
});
