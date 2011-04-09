/**
 * Important note: this application is not suitable for benchmarks!
 */

var http = require('http')
  , url = require('url')
  , fs = require('fs')
  , io = require('socket.io')
  , channels = require('socket.io-channels')
  , sys = require(process.binding('natives').util ? 'util' : 'sys')
  , port = 8001
  , server;

server = http.createServer(function(req, res){
    // doing nothing for now. socket.io will respond    
    res.writeHead(200, {'Content-Type': 'text/html'}); 

    var data = '';
    req.on('data', function(chunk) {
        data += chunk.toString();
    });

     req.on('end', function() {
         console.log(data);
         res.write(data);
         socket.broadcast(data);
     });
}),
server.listen(port);

// socket.io, I choose you
// simplest chat application evar
var socket = io.listen(server)
    channel = channels.listen(socket, {})
var buffer = [];

channel.on('connectedToChannel', function(client, sessionInfo){
  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has entered the Room"})

  // Send the buffer to the channel upon connecting. Will this send to everyone? Probably
  //channel.broadcastToChannel('chat', sessionInfo.channelId, {buffer: buffer});
})

channel.on('disconnectedFromChannel', function(sessionId, sessionInfo){
  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has left the Room"})
})

channel.on('chat',function(client, msg){
  // broadcast the chat message to everyone in the channel,
  // except the person who sent it:
  channel.broadcastToChannel('chat', msg.channelId, msg, client.sessionId)
  var msg = {channelId: msg.channelId, message: [client.sessionId, msg]};
  buffer.push(msg);

  // Broadcast context data to all clients about this message
  // TODO: get this context from django...somehow
  var context = {
    message: msg,
    postrank: {},
    video: {},
    image: {},
  }
  channel.broadcastToChannel('context', msg.channelId, context)
})


