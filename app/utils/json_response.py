from utils.json_encoder import JSONEncoder
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    def __init__(self, data):
        content = JSONEncoder().encode(data)
        # NOTE: An attempt to use mimetype='application/json; charset=UTF-8'
        #       failed in Internet Explorer (error code: c00ce56e)
        super(JsonResponse, self).__init__(content=content, mimetype='application/javascript') 
