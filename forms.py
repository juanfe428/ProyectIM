from wtforms import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
    username = StringField('',
    	[validators.length(min=4,max=25,message='Igrese un username valido')])
    password =PasswordField('',[
        validators.DataRequired(),

        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm=PasswordField('')
class LoginForm(Form):
	username=StringField('',[validators.length(min=4,max=25,message='Igrese un username valido')])
	password =PasswordField('',[validators.DataRequired()])