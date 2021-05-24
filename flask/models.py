from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
  __tablename__ = 'students'
  def __init__(self, id, name, age, email):
    self.id = id
    self.name = name
    self.age = age
    self.email = email

  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'email': self.email
    }

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  age = db.Column(db.Integer, unique=False, nullable=False)
