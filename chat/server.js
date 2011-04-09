/**
 * Important note: this application is not suitable for benchmarks!
 */

var http = require('http')
  , url = require('url')
  , fs = require('fs')
  , io = require('socket.io')
  , channels = require('socket.io-channels')
  , context_api = require('context_api').ContextApi()
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
var user_buffer = []; // list of users in the chat room.

/* Buffer format:
 *
 * {channelId: <channelId>, message: [client.sessionId, message])
 * */

channel.on('connectedToChannel', function(client, sessionInfo){
  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has entered the Room"})

  // Send the buffer to the channel upon connecting. Will this send to everyone? Probably
  console.log(buffer);
  channel.broadcastToChannel('chat', sessionInfo.channelId, {buffer: buffer},  client.sessionId);
})

channel.on('disconnectedFromChannel', function(sessionId, sessionInfo){
  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has left the Room"})
})

channel.on('chat',function(client, msg){
  // broadcast the chat message to everyone in the channel,
  // except the person who sent it:
  channel.broadcastToChannel('chat', msg.channelId, msg, client.sessionId)

  // push the message to the buffer to preload messages on new users.
  //var msg = {channelId: msg.channelId, message: msg, sessionId: client.sessionId};
  buffer.push(msg);

  // Broadcast context data to all clients about this message
  // TODO: get this context from django...somehow

  context_api.getContext(msg, function contextReceived(err, context) {
      channel.broadcastToChannel('context', msg.channelId, context)
  })
})


