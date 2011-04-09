/**
 * Important note: this application is not suitable for benchmarks!
 */

var http = require('http')
  , url = require('url')
  , fs = require('fs')
  , io = require('socket.io')
  , channels = require('socket.io-channels')
  , context_api = require('./context_api').ContextApi()
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
var dictBuffer = {}; // organized by chat room.
var getContext = true;

/* Buffer format:
 *
 * {channelId: <channelId>, message: [client.sessionId, message])
 * */
var userBuffer = []; // list of users in all chat rooms.

channel.on('connectedToChannel', function(client, sessionInfo){
  userBuffer.push(client.sessionId);
  var _localUserBuffer = JSON.parse(JSON.stringify(userBuffer));

  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has entered the Room"})

  
  _data = dictBuffer[sessionInfo.channelId];

  console.log(_data);
 
  // Send this buffer only to the new client.
  currentUserIndex = _localUserBuffer.indexOf(client.sessionId);
  console.log(currentUserIndex);
  _localUserBuffer.splice(currentUserIndex, 1);
  console.log("Exclude", _localUserBuffer);

  if (_data) {
      channel.broadcastToChannel('chat', sessionInfo.channelId, {buffer: _data}, _localUserBuffer);
  }
})

channel.on('disconnectedFromChannel', function(sessionId, sessionInfo){
  channel.broadcastToChannel('announcement',sessionInfo.channelId, {announcement: sessionInfo.session.username + " has left the Room"})

  console.log("Is leaving", sessionId);
  userBuffer.splice(userBuffer.indexOf(sessionId), 1)
})

channel.on('chat',function(client, msg){
  // broadcast the chat message to everyone in the channel,
  // except the person who sent it:
  console.log("Message is", msg);
  channel.broadcastToChannel('chat', msg.channelId, msg, client.sessionId)

  // push the message to the buffer to preload messages on new users.
  if (!dictBuffer[msg.channelId]) {
      dictBuffer[msg.channelId] = [];
  }
  dictBuffer[msg.channelId].push(msg);

  console.log(dictBuffer);

  // Broadcast context data to all clients about this message
  if(getContext) {
    context_api.getContext(msg, function contextReceived(err, context) {
        console.log('contextReceived');
        channel.broadcastToChannel('context', msg.channelId, context)
    })
  }
})


