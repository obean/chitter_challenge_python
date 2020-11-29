import unittest
import os
import json
from app import create_app, db

class UserTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app(config_name="testing")
    self.client = self.app.test_client
    self.user = {'username': 'testUser', 'password': 'testUser'}

    with self.app.app_context():
      db.create_all()

  def test_user_signup(self):
    res = self.client().post('/signup/', data=self.user)
    self.assertEqual(res.status_code, 201)
    # self.assertIn('testUser', str(res.data))

    # last line commented out, not sure if we wan't 201 as we aren't building  just an api, we are building a web app which renders pages itself, will have to check and see whether we want the same codes, job for tomorrow