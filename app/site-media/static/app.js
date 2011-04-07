if(typeof TWITTER_USERNAME != 'undefined') {
    var username = TWITTER_USERNAME;
    var userimage = TWITTER_IMAGE;
}else {
    var username = "Anonymous";
    var userimage = '';
}


var channel = new SocketIOChannel({
    host: window.location.hostname,
    port: SOCKET_PORT,
    // get channelId from url, we assume an ending slash /
    channelId: window.location.href.split("/").splice(-2)[0],

    session: {username: username, userimage: userimage},

    reconnectOnDisconnect: true,
    reconnectRetryInterval: 1000 * 10
});


function message(obj) {
    console.log('message', obj);
    var image = '';
    if(userimage) {
        var image = "<img class='twitter-icon' src='"+ obj.userimage + "' width=25 height=25>";
    }
    
    $("#messages").append("<div class='chat-message'>" + image + "<span>" + obj.username + "</span>" + " - " + obj.message + "</div>");
    $("#chatinput").val("");

};

function send() {
    console.log('send');
    var val = $("#chatinput").val();
    obj = {message: val, username: username, userimage: userimage};
    channel.send('chat', obj)
    message(obj);
};

function renderPostRank(data) {
    console.log('renderPostRank', data);
    return $(ich.postrank(data.postrank).embedly());
}

function renderPixMatch(data) {
    console.log('renderPixMatch', data);

    var ul = $("<ul>");

    for (var i in data.pixmatch.results) {
        ul.append(ich.pixmatch_derive({label: data.pixmatch.results[i]})[0]);
    }

    // hack!!!
    $("#stream").append(ul[0]);

    return ich.pixmatch({list: ul[0]});
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
    scrollMessages();
});

function scrollMessages() {
 
    $('#messages').animate({
        scrollTop: $('#messages div:last').offset().top
    }, 2000);
    
}

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
