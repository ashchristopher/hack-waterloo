"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from api.idee import PixMatch

class PixMatchTest(TestCase):
    def test_basic(self):
    	p = PixMatch()
    	url = 'http://www.google.ca/images/logos/ps_logo2.png'
    	output = p.process(url)
    	print output
