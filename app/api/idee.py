import urllib
from urllib import urlencode
import os
import subprocess
from django.conf import settings
from django.utils import simplejson
from django.core.urlresolvers import reverse

from api import Api

class PixMatch(Api):
    
    @staticmethod
    def process(data):
        api_url = "http://pixmatch-r.hackdays.tineye.com/rest/"
        local_context = {
            'pixmatch' : [],
        }
        if not (data.endswith('.jpg') or data.endswith('.png')):
            #empty dict added
            return {}

        try:
            filename = data.split(os.path.sep)[-1]
            output_path = os.path.join(settings.MEDIA_ROOT, 'dynamic', 'images')

            # store the data locally
            cmd = "wget %s -N --directory-prefix=%s" % (data, output_path)
            os.system(cmd)
            file_path = "%s/%s" %(output_path, filename)

            # curl the file to idee
            cmd = 'curl %s -F method=search -F image=@%s;filename=query.jpg' % (api_url, file_path)
            output = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE).communicate()[0]
            json = simplejson.loads(output)
            
            for result in json.get('result', []):
                f = result.get('filename')
                f = f.lstrip('/gackers_')
                url = reverse('media', kwargs={'path' : 'static/images/memes/%s' % f})
                local_context['pixmatch'].append(url)
                
        except Exception, e:
            raise(e)
        return local_context