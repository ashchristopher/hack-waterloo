"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson

from api.idee import PixMatch, Piximilar
from api.pipeline import Pipeline

class PiximilarTest(TestCase):
    def test_basic(self):
        p = Piximilar()
    	url = "http://localhost:8000/site-media/static/images/memes/HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"
        output = p.process(url)

        print output

class PixMatchTest(TestCase):
    def test_basic(self):
    	p = PixMatch()
    	url = "http://dev:8000/site-media/static/images/memes/HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"
    	output = p.process(url)
    	print output
    	
    def test_json(self):
        ret = '{"status": "ok", "method": "search", "result": [{"score": "98.2", "filename": "/gackers_HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"}, {"score": "97.7", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-POSTRANK.jpg"}, {"score": "97.6", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-CASTROLLER.jpg"}, {"score": "97.6", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-YELLOWPAGES.jpg"}, {"score": "97.5", "filename": "/gackers_HACKWATERLOO-Y-U-NO-USE-FRESHBOOKS.jpg"}, {"score": "96.6", "filename": "/gackers_HackWaterloo-Y-U-NO-MAKE-RESERVATION-SYSTEM.jpg"}], "error": []}'
        json = simplejson.loads(ret)
        
    def test_pipeline_pixmatch(self):
        print "\n\n\n\n\n\n"
        p = Pipeline()
        msg = "http://dev:8000/site-media/static/images/memes/HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg"
        output = p.run(msg)
        print output
        
    def test_pipeline_postrank(self):
        print "\n\n\n\n\n\n"
        p = Pipeline()
        msg = "http://www.igvita.com/2011/04/07/life-beyond-http-11-googles-spdy/"
        output = p.run(msg)
        print output 
        
        
    def test_re(self):
        print "\n\n\n\n\n---------- TESTING RE---------"
    	p = PixMatch()
    	url = "Check out this picture yo! http://dev:8000/site-media/static/images/memes/HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg its awesome/."
    	output = p.run(url)
    	print output