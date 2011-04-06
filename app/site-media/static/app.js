var username = "User_" + new Date().getTime();

var channel = new SocketIOChannel({
    host: window.location.hostname,
    port: SOCKET_PORT,
    // get channelId from url, we assume an ending slash /
    channelId: window.location.href.split("/").splice(-2)[0],

    session: {username: username},

    reconnectOnDisconnect: true,
    reconnectRetryInterval: 1000 * 10
});


function message(obj) {
    console.log('got message', obj);
    $("#messages").append("<div>From:" + obj.username + " - " + obj.message + "</div>");
    $("#chatinput").val("");

};

function send() {
    console.log('send');
    var val = $("#chatinput").val();
    obj = {message: val, username: username};
    channel.send('chat', obj)
    message(obj);
};

channel.on('chat', function(obj) {
    if ('buffer' in obj ) {
        for (var i in obj.buffer) {
            message(obj.buffer[i]);
        }
    } else {
        message(obj);
    }

});

channel.on('announcement', function(obj) {
    console.log("Announcement", obj);
    $("#messages").append("<div>" + obj.announcement + "</div>");
});

channel.on('context', function(obj) {
    console.log("Context", obj);
    //$("#messages").append("<div>" + obj.announcement + "</div>");
});      

channel.on('connect', function(obj) {
    console.log('Connected!');
});

$(document).ready(function () {
    $("#chatinput").focus();

    $("#chatform").submit(function() {
        send();
        return false;
    });
});
