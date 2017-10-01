from flask import Flask
from flask import render_template
from flask import request,url_for,redirect
from flask_wtf import CSRFProtect
from flask import flash

from config import DevelopmentConfig
from models import db
from models import User
import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route('/', methods=['GET','POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    title = 'Curso Flask'
    if request.method== 'POST' and comment_form.validate():
    	
    	user=User(comment_form.username.data,
    			  comment_form.password.data)
    	db.session.add(user)
    	db.session.commit()
    else:
        error="hola"
        flash(error)
    return render_template('index.html', title=title, form=comment_form)
    

@app.route('/login',methods=['GET','POST'])
def login_page():
    comment_form = forms.LoginForm(request.form)
    if request.method== 'POST' and comment_form.validate():


        username=comment_form.username.data
        password=comment_form.password.data

        user=User.query.filter_by(username=username).first_or_404()

        if User is not None and user.verify_password(password)==True:

            pass
            mensaje='Bienvenido'
            flash(mensaje)
            return redirect(url_for('home'))
        else:
            MensajeError='usuario o contraseña no valida'
            flash(MensajeError)


    return render_template("login.html",form=comment_form)
@app.route('/home')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))
if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
    	db.create_all()
    app.run(port=8000)
