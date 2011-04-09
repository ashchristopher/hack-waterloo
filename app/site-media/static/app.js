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
    console.log('message', obj);
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

function renderPostRank(data) {
    console.log('postrank_render');
    var postrank = data.postrank;
    // TODO: replace with icanhaz template?
    return ['<div>',
        '<h4>Post Rank</h4>',
        '<a href="', postrank.url, '">url</a>',
        '<span class="rank">', postrank.rank, '</span>',
    '</div>'].join('');
}

function contextReceived(context) {
    console.log("contextReceived", context);
    var items = [];
    if(context['postrank']) {
        items.push(renderPostRank(context));
    }
    $("#stream").append(items.join('')); 
}

function announcementReceived(obj) {
    console.log("Announcement", obj);
    $("#messages").append("<div>" + obj.announcement + "</div>");
}

channel.on('chat', function(obj) {
    console.log("Got chat", obj);
    if ('buffer' in obj ) {
        for (var i in obj.buffer) {
            message(obj.buffer[i]);
        }
    } else {
        message(obj);
    }

});

channel.on('announcement', announcementReceived);
channel.on('context', contextReceived);      
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
