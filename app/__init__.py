from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
  from app.models import User
  app = Flask(__name__, instance_relative_config=True, template_folder='./static') 
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.app_context().push()
  db.init_app(app)
  

  @app.route('/')
  def login_signup():
   # return "HELLOWORLD"
    return render_template('signup.html')

  @app.route('/signup', methods=["POST"])
  def signup():
    user = User(username=request.form['username'], password=request.form['password'])
    user.save()
    session["current_user"] = user.username
    return redirect('/feed')
    



  return app  