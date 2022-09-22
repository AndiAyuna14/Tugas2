from http import client
from multiprocessing.connection import Client
from django.test import TestCase , Client
from django.urls import reverse
from mywatchlist.views import *

# Create your tests here.

class html_mywatchlist(TestCase):
    def test_url_exist_at_correct_location(self):
        response = Client().get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(response.status_code, 200)

class xml_mywatchlist(TestCase):
    def test_url_exist_at_correct_location(self):
        response = Client().get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)

class json_mywatchlist(TestCase):
    def test_url_exist_at_correct_location(self):
        response = Client().get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)
