import re
import urllib
from urllib import urlencode
import os
import subprocess
from django.conf import settings
from django.utils import simplejson
from django.core.urlresolvers import reverse

from api import Api

class Piximilar(Api):
    @staticmethod
    def process(data):
        api_url = "http://piximilar.hackdays.tineye.com/rest/"
        local_context = {
            'piximilar': {},
        }

        try:
            data = re.search("(?P<url>https?://[^\s]+)", data).group("url")
            if not (data.endswith('.jpg') or data.endswith('.png')):
                #empty dict added
                return {}
            
            filename = data.split(os.path.sep)[-1]
            output_path = os.path.join(settings.MEDIA_ROOT, 'dynamic', 'images')

            # store the data locally
            cmd = "wget %s -N --directory-prefix=%s" % (data, output_path)
            os.system(cmd)
            file_path = "%s/%s" %(output_path, filename)

            # curl the file to idee
            cmd = 'curl %s -F method=visual_search -F image=@%s' % (api_url, file_path)
            output = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE).communicate()[0]
            json = simplejson.loads(output)
            
            local_context['piximilar'].update({
                'original' : data,
                'results' : [],
            })


            for result in json.get('result', []):
                # figure out what else to do with this?
                local_context['piximilar']['results'].append(result)
                
        except Exception, e:
            raise(e)
        return local_context


class PixMatch(Api):
    
    @staticmethod
    def process(data):
        api_url = "http://pixmatch-r.hackdays.tineye.com/rest/"
        local_context = {
            'pixmatch' : {},
        }
        
        try:
            data = re.search("(?P<url>https?://[^\s]+)", data).group("url")
            if not (data.endswith('.jpg') or data.endswith('.png')):
                #empty dict added
                return {}
            
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
            
            local_context['pixmatch'].update({
                'original' : data,
                'results' : [],
            })
            
            for result in json.get('result', []):
                f = result.get('filename')
                f = f.lstrip('/gackers_')
                url = reverse('media', kwargs={'path' : 'static/images/memes/%s' % f})
                local_context['pixmatch']['results'].append(url)
                
        except Exception, e:
            raise(e)
        return local_context
