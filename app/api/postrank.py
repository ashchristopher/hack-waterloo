import urllib
import json

from api import Api
from api.idee import Helper

API_KEY = 'hackwaterloo'
METRIC_URL = 'http://api.postrank.com/v2/entry/metrics?appkey=%s&' % (API_KEY,)

class PostrankApi(Api):
    
    @staticmethod
    def process(data):
        data = Helper.parse_url(data)
        if (data.endswith('.jpg') or data.endswith('.png')):
            return {}

        try:
            openurl = urllib.urlopen('%sid=%s' % (METRIC_URL, data))
            content = json.loads(openurl.read())
            content[data]['url'] = data
            response = {
                'postrank': content[data],
            }
            return response
        except:
            return {}
