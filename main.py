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

#Carga los usaurios ya registrados de un archivo texto
f=open("usuarios.txt","r")
texto=f.readlines()
f.close()
for palabrasos in texto:
    palabras=palabrasos.split("-")
    for usuario in palabras:
        if usuario!= "":
            usuarios.append(usuario)

#carga las contraseñas de un archivo texto
f=open("passwords.txt","r")
texto=f.readlines()
f.close()
for palabrasos in texto:
    palabras=palabrasos.split("-")
    for pswd in palabras:
        if pswd!= "":
            passwords.append(pswd)

@app.route('/register', methods=['GET','POST'])


def index():
    global usuarios,passwords
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
            f=open("usuarios.txt","a")
            f.write(str(usuario)+"-")
            f.close()
            f=open("passwords.txt","a")
            f.write(str(password)+"-")
            f.close()
                


    return render_template('index.html', title=title, form=formulario)
    

@app.route('/login',methods=['GET','POST'])
def login_page():
    global usuarios,passwords
    title = 'Tellme!'
    formulario = forms.LoginForm(request.form)
    usuario=formulario.username.data
    password=formulario.password.data
    if request.method== 'POST' and formulario.validate():
        if usuario in usuarios and password in passwords:
        
            if usuarios.index(usuario)==passwords.index(password):
                bandera=True
                return redirect(url_for('home'))
            else:
                flash("usuario o contrasena incorrecta")
        else:

            flash('Contrasena o usario incorrecto')

    return render_template("login.html",form=formulario,title=title)
@app.route('/home',methods=['GET','POST'])

def home():
    pass
    formulario = forms.LoginForm(request.form)
    return render_template("home.html", form=formulario)
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)
