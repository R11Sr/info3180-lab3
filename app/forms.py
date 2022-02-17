from ast import For
from flask_wtf import Form
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import StringField,TextAreaField
from wtforms.validators import DataRequired,Email

class ContactForm(Form):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])






    

