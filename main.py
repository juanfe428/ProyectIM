from flask import Flask,session
from flask import render_template
from flask import request,url_for,redirect
from flask_wtf import CSRFProtect
from flask import flash

import forms
import json

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

usuarios=[]
passwords=[]
@app.route('/register', methods=['GET','POST'])


def index():
    formulario = forms.CommentForm(request.form)
    title = 'Tellme!'
    usuario=formulario.username.data
    password=formulario.password.data
    
    if request.method== 'POST' and formulario.validate():
        if usuario in usuarios:
            flash("El usuario ya existe")
        else:
            usuarios.append(usuario)
            passwords.append(password)
            flash("Se ha registrado")
                
        print(usuarios)
        print(passwords)
    return render_template('index.html', title=title, form=formulario)
    

@app.route('/login',methods=['GET','POST'])
def login_page():
    title = 'Tellme!'
    formulario = forms.LoginForm(request.form)
    usuario=formulario.username.data
    password=formulario.password.data
    if request.method== 'POST' and formulario.validate():
        if usuario in usuarios and password in passwords:
            if usuarios.index(usuario)==passwords.index(password):
                return redirect(url_for('home'))
            else:
                flash("usuario o contraseña incorrecta")
        else:

            flash('Contraseña o usario incorrecto')

    return render_template("login.html",form=formulario,title=title)
@app.route('/home',methods=['GET','POST'])

def home():
    pass
    formulario = forms.LoginForm(request.form)
    return render_template("home.html", form=formulario)
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)
