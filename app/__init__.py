import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view='login'
oid = OpenID(app,os.path.join(basedir,'tmp'))

from .moment import momentjs
app.jinja_env.globals['momentjs'] = momentjs

from app import views,models

from flask.ext.mail import Mail
mail = Mail(app)

