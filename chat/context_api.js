var http = require('http');
var EventEmitter = require('events').EventEmitter;

exports.ContextApi = function() {

    var self = this;
    var django_server = 'http://localhost:8000'

    /**
     * Send the message to django context api
     */
    function getContext(message, callback)
    {
        console.log('getContext');
        var client = http.createClient(8000, django_server);
        var request = client.request('POST', '/api/context/', message);

        request.addListener("response", function(response) { 
            var body = "";

            response.addListener("data", function(data) {
                body += data;
            });

            response.addListener("end", function() { 
                // send the context to the callback function
                console.log('Django context api response received');
                callback({}, body);
                //var response = JSON.parse(body); 
            });
        });

    }

    return {
        'getContext': getContext,
    }

    EventEmitter.call(this);
}
