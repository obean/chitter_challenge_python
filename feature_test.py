import unittest
import os
# import json
#  1 from flask import Flask, render_template, request, redirect, flash, session, Markup
from app import create_app, db, models
import capybara
import capybara.dsl

#pytest_plugins = ['capybara.pytest_plugin']


# def test_home_page(page):
#   page.visit('/')



# print('potato')
# # import capybara
# # import capybara.dsl
# import unittest

class CapybaraTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app(config_name="testing")
    self.app.secret_key = os.getenv('SECRET')
    self.client = self.app.test_client()

    self.page = capybara.dsl.page
    capybara.app = self.app
    models.User('testUser','testUserPassword').save()
   # db.session.add(self.user).commit()
    with self.app.app_context():
      db.create_all()
      
  def sign_in(self):
    self.page.visit('/')
    self.page.find("#sign_in_box").fill_in("username", value="testUser")
    self.page.find("#sign_in_box").fill_in("password", value="testUserPassword")
    self.page.find("#sign_in_box").click_button('submit')
        

  def tearDown(self):
    capybara.reset_sessions() 
   # db.session.query(models.User).delete() 
    models.User.query.delete()
    db.session.commit()
    
    
    



  def test_valid_signup(self):
    """ user can signup """
    self.page.visit('/')
    self.page.find("#sign_up_box").fill_in("username", value="testUser1")
    self.page.find("#sign_up_box").fill_in("password", value="password")
    self.page.find("#sign_up_box").click_button('submit')
    assert self.page.has_text("Peeps")
    assert self.page.has_text("Create Peep")

  def test_valid_signin(self):
    """signed up user can log in"""
    self.page.visit('/')
    self.page.find("#sign_in_box").fill_in("username", value="testUser")
    self.page.find("#sign_in_box").fill_in("password", value="testUserPassword")
    self.page.find("#sign_in_box").click_button('submit')
    assert self.page.has_text("Peeps")
    assert self.page.has_text("Create Peep")
  
  def test_invalid_signup_wrong_username(self):
    self.page.visit('/')
    self.page.find("#sign_in_box").fill_in("username", value="not_testUser")
    self.page.find("#sign_in_box").fill_in("password", value="testUserPassword")
    self.page.find("#sign_in_box").click_button('submit')
    assert self.page.has_text('incorrect username, try again')

  def test_invalid_signup_wrong_password(self):
    self.page.visit('/')
    self.page.find("#sign_in_box").fill_in("username", value="testUser")
    self.page.find("#sign_in_box").fill_in("password", value="not_testUserPassword")
    self.page.find("#sign_in_box").click_button('submit')
    assert self.page.has_text('incorrect password, try again')

  def test_cannot_peep_not_signed_in(self):
    self.page.visit('/feed')
    self.page.fill_in("new_peep", value="this is a mighty fine test peep")
    self.page.click_button("peep it!")
    self.page.fill_in("new_peep", value=" ")
    assert not self.page.has_text('this is a mighty fine test peep')
    assert self.page.has_text('You must be logged in to post, click here to log in')

  def test_can_peep_when_signed_in(self):
    self.sign_in()
    self.page.fill_in("new_peep", value="this is a test peep")
    self.page.click_button("peep it!")
    assert self.page.has_text('this is a test peep')
    assert not self.page.has_text('You must be logged in to post, click here to log in')

  def test_peeps_are_arranged_chronologically(self):
    self.sign_in()
    self.page.fill_in("new_peep", value="this is the first test peep")
    self.page.click_button("peep it!")
    self.page.fill_in("new_peep", value="this is the second test peep")
    self.page.click_button("peep it!")
    capybara.match = "first"
    assert self.page.find(".peep").has_text('this is the second test peep')
    assert not self.page.find(".peep").has_text('this is the first test peep')

    if __name__ =="__main__":
      unittest.main()    