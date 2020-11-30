import unittest
import os
import json

from app import create_app, db, models

class UserTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app(config_name="testing")
    self.app.secret_key = os.getenv('SECRET')
    self.client = self.app.test_client()
    self.user = {'username': 'testUser', 'password': 'testUser'}

    with self.app.app_context():
      db.create_all()

  def test_index_page(self):
    """Test server can load homepage"""
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)
    self.assertIn( b"sign up\n<form", res.data)
    self.assertIn( b"sign in\n<form", res.data)

  def test_user_signup(self):
    res = self.client.post('/signup', data=self.user)
    print(res.data)
    self.assertIn(b"Redirect", res.data)
    self.assertEqual(res.status_code, 302)
    
    


    if __name__ =="__main__":
      unittest.main()