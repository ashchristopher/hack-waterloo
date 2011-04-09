import urllib
from urllib import urlencode
import os

from django.conf import settings

from api import Api

class PixMatch(Api):
	
    api_url = "http://pixmatch-r.hackdays.tineye.com/rest/"
	
    def process(self, data):
        local_context = {}
        if not (data.endswith('.jpg') or data.endswith('.png')):
            #empty dict added
            return {}

        try:
            output_path = os.path.join(settings.MEDIA_ROOT, 'dynamic', 'images')
            print output_path
            os.system("wget %s -N --directory-prefix=%s" % (data, output_path))
            # wget http://www.google.ca/images/nav_logo40.png --directory-prefix=foo/
            # 
            # openurl = urllib.urlopen('%sid=%s' % (METRIC_URL, url))
        except Exception, e:
            raise(e)
        return local_context