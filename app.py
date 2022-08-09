import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template

app = Flask(__name__)
env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from commands import process_option


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subways')
def subways():
    return render_template('subways.html')

@app.route('/streets')
def streets():
    return render_template('streets.html')

@app.route('/data/<option>')
def options(option):
    return process_option(option, db)

if __name__ == '__main__':
    main()
