from flask import Flask,session
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
Usuario=False
@app.route('/register', methods=['GET','POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    title = 'Tellme!'
    flash('SDASD')
    if request.method== 'POST' and comment_form.validate():
    	
    	user=User(comment_form.username.data,
    			  comment_form.password.data)
    	db.session.add(user)
    	db.session.commit()
        
    return render_template('index.html', title=title, form=comment_form)
    

@app.route('/login',methods=['GET','POST'])
def login_page():
    title = 'Tellme!'
    error=None
    comment_form = forms.LoginForm(request.form)
    if request.method== 'POST' and comment_form.validate():

        username=comment_form.username.data
        password=comment_form.password.data

        user=User.query.filter_by(username=username).first_or_404()

        if User is not None and user.verify_password(password)==True:
            pass
            mensaje='Bienvenido'
            flash(mensaje)
            Usuario=True

            return redirect(url_for('home'))

        else:

            error = 'Contraseña o usario incorrecto'

    return render_template("login.html",form=comment_form,title=title,error=error)

@app.route('/home',methods=['GET','POST'])
def home():
    pass
    comment_form = forms.LoginForm(request.form)
    if request.method== 'POST':
        username=comment_form.username.data
        user=User.query.filter_by(username=username).first_or_404()
        return redirect(url_for('hola'))
    return render_template("home.html", form=comment_form)
@app.route('/prueba')
def hola():
    return render_template("error.html")

@app.errorhandler(404)
def page_not_found(e):
    
    return render_template("error.html")
if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
    	db.create_all()
    app.run(port=8000)
