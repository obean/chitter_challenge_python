from app import db


class User(db.Model):
  """ User Model """
  __tablename__ = "chitter_users"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(25), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)

  def __init__(self, name):
        """initialize with name."""
        self.name = name

  def save(self):
      db.session.add(self)
      db.session.commit()

  @staticmethod
  def get_all():
      return Bucketlist.query.all()

  def delete(self):
      db.session.delete(self)
      db.session.commit()


  # The __repr__ method represents the object instance of the model whenever it is queries.
  def __repr__(self):
    return "<User: {}>".format(self.name)