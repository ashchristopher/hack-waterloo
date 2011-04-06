var http = require('http');

exports.ContextApi = function() {

    var self = this;
    var django_server = 'localhost';
    var django_port = 8000;
    var api_path = '/api/context/'

    /**
     * Send the message to django context api
     */
    function getContext(message, callback)
    {
        console.log('getContext', message);
        var client = http.createClient(django_port, django_server);
        var buf = [];
        for(var i in message) {
            buf.push(i + '=' + message[i]);
        }
        var post_data = buf.join('&');//JSON.stringify(message);
 
        var headers = {
            'Host': django_server,
            'Content-Type': 'application/json',
            'Content-Length': post_data.length
        };
        var request = client.request('POST', api_path, headers);
        console.log(post_data);
        request.write(post_data);

        request.on('response', function(response) { 

            console.log("response: "+response.statusCode);
            var body = "";
            response.on("data", function(chunk) {
                body += chunk;
            });

            response.on("end", function() { 
                // send the context to the callback function
                if(response.statusCode === 200) {
                    var data = JSON.parse(body);
                    data['message'] = message;
                    callback({}, data);
                } else {
                    console.log(body);
                    callback({'status_code': response.statusCode, 'body': body}, {});
                }
            });
        });
        request.end();

    }

    return {
        'getContext': getContext,
    }

}
