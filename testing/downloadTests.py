import unittest
import os
from flask import Flask
from app import app

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True

        def test_download(self):
            response = self.client.get('/download')

            #Checking status code for 200
            self.assertEqual(response.status_code, 200)

            #Check for correct content type
            self.assertEqual(response.headers['Content-Type'], 'application/octet-stream')

            #Check for correct header of Content-Disposition
            filename = os.path.basename(response.headers['Content-Disposition'].split('filename=')[1])
            self.assertEqual(filename, 'test.zip')

            #Check that file data is not empty
            self.assertTrue(len(response.data) > 0)
