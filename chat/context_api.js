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
        console.log('getContext');
        var client = http.createClient(django_port, django_server);
        client.on('error', function(err) {
            console.log(err);
        });

        var request = client.request('GET', api_path, {'host':django_server});
        request.on('response', function(response) { 

            console.log("response: "+response.statusCode);

            var body = "";
            response.on("data", function(chunk) {
                body += chunk;
            });

            response.on("end", function() { 
                // send the context to the callback function
                var data = JSON.parse(body);
                data['message'] = message;
                console.log('Django context api response received:');
                console.log(data);
                callback({}, data);
            });
        });

        request.end();

    }

    return {
        'getContext': getContext,
    }

}
