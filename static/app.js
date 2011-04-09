var username = "User_" + new Date().getTime();

var channel = new SocketIOChannel({
    host: "localhost",
    port: 8000,
    channelId: "foofoo",

    session: {username: username},

    reconnectOnDisconnect: true,
    reconnectRetryInterval: 1000 * 10 // try to reconnect every 30 seconds

    function message(obj) {
        $("#messages").append("<div>" + obj.message[0] + ", " + obj.message[1] + "</div>");

    }

    function send() {
        var val = $("#textinput").val();
        channel.send('chat', {message: val username: username});
    };

    channel.on('chat', function(obj) {
        message(obj);
    });

    channel.on('connect', function(obj) {
        console.log('Connected!');

    });
});

/*
 *
 * The front end will need to be able to specify the channel based on some output from the django
 * app?
 * */

$(document).ready(function () {
    $("#chatform").submit(function() {
        send();
        message({ message: ['you', val]);

        return false;
    });
});
