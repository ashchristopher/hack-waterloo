var username = "User_" + new Date().getTime();

var channel = new SocketIOChannel({
    host: "localhost",
    port: 8001,
    channelId: window.location.href.split("/").splice(-2)[0],

    session: {username: username},

    reconnectOnDisconnect: true,
    reconnectRetryInterval: 1000 * 10
});


function message(obj) {
    $("#messages").append("<div>From:" + obj.username + " - " + obj.message + "</div>");
    $("#chatinput").val("");

};

function send() {
    var val = $("#chatinput").val();
    obj = {message: val, username: username};
    channel.send('chat', obj)
    message(obj);
};

channel.on('message', function(obj) {
    console.log('got a msg new', obj);
});

channel.on('chat', function(obj) {
    if ('buffer' in obj ) {
        for (var i in obj.buffer) {
            message(obj.buffer[i]);
        }
    } else {
        console.log("Single message");
        console.log(obj);
        message(obj);
    }

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
