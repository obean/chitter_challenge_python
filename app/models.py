from app import db
import time
from datetime import datetime
from sqlalchemy import desc

class User(db.Model):
  """ User Model """
  __tablename__ = "chitter_users"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)

  def __init__(self, username, password):
        """initialize with name."""
        self.username = username
        self.password = password

  def save(self):
      db.session.add(self)
      db.session.commit()

  @staticmethod
  def get_all():
      return User.query.all()

  def find_one(user):
    return User.query.filter_by(username=user).first()    

  def delete(self):
      db.session.delete(self)
      db.session.commit()


  # The __repr__ method represents the object instance of the model whenever it is queries.
  def __repr__(self):
    return f"<User: {self.username}>"

class Peep(db.Model):
  """Peep Model"""
  __tablename__ = "peeps"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25), unique=False, nullable=False)
  peep = db.Column(db.String(240), unique=False, nullable=False)
  time = db.Column(db.DateTime(), default=datetime.now())

  def __init__(self, username, peep):
      """initialize with name."""
      self.username = username
      self.peep = peep

  def save(self):
      db.session.add(self)
      db.session.commit()

  @staticmethod
  def get_all():
      return Peep.query.order_by(Peep.time.desc()).all()

  def delete(self):
      db.session.delete(self)
      db.session.commit()


  # The __repr__ method represents the object instance of the model whenever it is queries.
  def __repr__(self):
    return f"<Peep: {self.id} {self.username}, {self.peep}, {self.time}>"