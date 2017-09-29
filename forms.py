from wtforms import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from models import User


class CommentForm(Form):
    username = StringField('',
    	[validators.length(min=4,max=25,message='Igrese un username valido')])
    password =PasswordField('',[
        validators.DataRequired(),

        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm=PasswordField('')

    def validate_username(form,field ):
    	username=field.data 
    	user=User.query.filter_by(username=username).first()
    	if user is not None:
    		raise validators.ValidationError("El usuario esta registrado")


class LoginForm(Form):
	username=StringField('',[validators.length(min=4,max=25,message='Igrese un username valido')])
	password =PasswordField('',[validators.DataRequired()])
