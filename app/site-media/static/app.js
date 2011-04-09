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
    console.log('renderPostRank', data);
    return $(ich.postrank(data.postrank).embedly());
}

function renderPixMatch(data) {
    console.log('renderPixMatch', data);
    var li = [];
    for (var i in data.pixmatch.results) {
        li[i] = ich.pixmatch_derive({label: data.pixmatch.results[i]});
    }
    var f = { list: li.join('')}  
    console.log(li.join(''));
    return ich.pixmatch();
}

function contextReceived(context) {
    // context can be a list of contexts or a single item
    console.log("contextReceived", context);
    var to_render = []; 
    if ('buffer' in context) {
        for (var i in context.buffer) {
            to_render.push(context.buffer[i]);
        }
    } else {
        to_render.push(context);
    }

    var items = [];
    for (var i in to_render) {
        if(to_render[i]['postrank']) {
            pushToStream(renderPostRank(to_render[i]));
        }
        
        if(to_render[i]['pixmatch']) {
            pushToStream(renderPixMatch(to_render[i]));
        }
    }
}

function pushToStream(obj) {
    $(obj).appendTo('#stream').wrap('<div/>'); 
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
