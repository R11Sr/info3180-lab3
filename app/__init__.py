from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
from app import views
app.config.from_object(Config)

mail = Mail(app)

#Enable CSRF protection globally for a Flask app.
csrf = CSRFProtect(app)
