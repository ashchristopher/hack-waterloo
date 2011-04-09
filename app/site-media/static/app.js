var username = "User_" + new Date().getTime();

var channel = new SocketIOChannel({
    host: "localhost",
    port: 8001,
    channelId: "foofoo",

    session: {username: username},

    reconnectOnDisconnect: true,
    reconnectRetryInterval: 1000 * 10
});


function message(obj) {
    $("#messages").append("<div>" + obj.message[0] + ", " + obj.message[1] + "</div>");
    $("#chatinput").val("");

};

function send() {
    var val = $("#chatinput").val();

    obj = {message: val, username: username};
    channel.send('chat', obj)
    message(obj);
};

channel.on('chat', function(obj) {
    console.log("got a response");
    message(obj);
});

channel.on('connect', function(obj) {
    console.log('Connected!');

});

/*
 *
 * The front end will need to be able to specify the channel based on some output from the django
 * app?
 * */

$(document).ready(function () {
    $("#chatform").submit(function() {
        send();
        return false;
        message({ message: ['you', val]});
    });
});
