"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson
from api.idee import PixMatch

class PixMatchTest(TestCase):
    def test_basic(self):
    	p = PixMatch()
    	url = "http://dev:8000/site-media/static/images/memes/HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"
    	output = p.process(url)
    	print output
    	
    def test_json(self):
        ret = '{"status": "ok", "method": "search", "result": [{"score": "98.2", "filename": "/gackers_HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"}, {"score": "97.7", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-POSTRANK.jpg"}, {"score": "97.6", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-CASTROLLER.jpg"}, {"score": "97.6", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-YELLOWPAGES.jpg"}, {"score": "97.5", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-FRESHBOOKS.jpg"}, {"score": "96.6", "filename": "/gackers_HackWaterloo-Y-U-NO-MAKE-RESERVATION-SYSTEM.jpg"}], "error": []}'
        json = simplejson.loads(ret)