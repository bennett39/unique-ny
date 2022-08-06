import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import SubwayLine


@app.route('/')
def index():
    return '<p>Hello, World!</p>'

@app.route('/add/<line_name>')
def add(line_name):
    line = SubwayLine(name=line_name)
    db.session.add(line)
    db.session.commit()
    return f'Added {line.name}'

@app.route('/list')
def list():
    lines = SubwayLine.query.all()
    return ','.join([l.name for l in lines])
