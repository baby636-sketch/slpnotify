from django.conf import settings
import json, requests
from main import tasks
import requests_mock
import pytest
import requests


class SLPDBTokenScannerTest(object):	

    def __init__(self, requests_mock, capsys):
		self.url = ''
		self.expectation = ''
        self.requests_mock = requests_mock
        self.capsys = capsys
        
    
    def test(self):
        self.requests_mock.get(self.url, text=self.expectation)
        captured = self.capsys.readouterr()
        assert captured.out == self.output
        