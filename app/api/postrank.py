import urllib
import json

from api import Api

API_KEY = 'hackwaterloo'
METRIC_URL = 'http://api.postrank.com/v2/entry/metrics?appkey=%s&' % (API_KEY,)

class PostrankApi(Api):
    def process(self, url):
        response = {}
        try:
            openurl = urllib.urlopen('%sid=%s' % (METRIC_URL, url))
            content = json.loads(openurl.read())
            response = {
                'success': True,
                'content': content,
                }
        except Exception as e:
            response = {
                'success': False,
                'error_message': e.value,
                }
        return json.dumps(response)
