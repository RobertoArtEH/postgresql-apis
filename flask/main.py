from flask import Flask
from flask import jsonify
from config import Config
from models import db, Students

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/students')
def index():
  students = [ student.json() for student in Students.query.all() ] 
  return jsonify({'students': students })