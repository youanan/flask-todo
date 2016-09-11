from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("config")

db = MongoEngine(app)
bootstrap = Bootstrap(app)


from app import views, models
