
/**
 * Module dependencies.
 */

require.paths.push('/Users/kawano_tomonori/.nvm/v0.4.9/lib/node_modules');

var express = require('express')
  , routes = require('./routes')
  , io  = require('socket.io')

var app = module.exports = express.createServer();

// Configuration
app.configure(function(){
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(__dirname + '/content'));
});

app.configure('development', function(){
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
});

app.configure('production', fujkknction(){
  app.use(express.errorHandler()); 
});

// Routes
app.get('/', function(req, res) {
    res.render('index', {
       title : 'tomox chat roooooom!!!'
    });
});


app.listen(3000);

// socket.io
var socket = io.listen(app);
socket.sockets.on("connection", function(client){
    client.on("chat", function(msg) {
        console.log("chat", msg);

        client.send(msg);
        client.broadcast.send(msg);
    });
    client.on("disconnect", function(msg){
       console.log("disconnect");
    });
});

console.log("Express server listening on port %d in %s mode", app.address().port, app.settings.env);
