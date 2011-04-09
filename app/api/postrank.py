import urllib
import json

from api import Api

API_KEY = 'hackwaterloo'
METRIC_URL = 'http://api.postrank.com/v2/entry/metrics?appkey=%s&' % (API_KEY,)

class PostrankApi(Api):
    def process(self, data):
        openurl = urllib.urlopen('%sid=%s' % (METRIC_URL, data))
        content = json.loads(openurl.read())
        response = {
            'postrank': content,
            }
        return response
