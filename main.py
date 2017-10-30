from flask import Flask,session
from flask import render_template
from flask import request,url_for,redirect
from flask_wtf import CSRFProtect
from flask import flash

import forms
import json

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.update(
    DEBUG=True,
    SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT',
    USERNAME="JUAN",
    PASSWORD="ADMIN"
)
usuarios=[]
passwords=[]
amigos=[[],[],[],[],[]]
Mensajes=[[],[],[],[],[],[],[]  ]


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
            i=0
          

    return render_template('index.html', title=title, form=formulario)
    

@app.route('/login',methods=['GET','POST'])
def login_page():

    global usuarios,passwords
    print(usuarios)
    title = 'Tellme!'
    formulario = forms.LoginForm(request.form)
    usuario=formulario.username.data
    password=formulario.password.data
    if request.method== 'POST' and formulario.validate():

        if usuario in usuarios and password in passwords:

            indice=usuarios.index(usuario)
            print(indice)

            print(passwords[indice])

            if passwords[indice]==password:
            #if usuarios.index(usuario)==passwords.index(password)  :
                i=0
                for user in usuarios:


                    if user==usuario:
                        print(i)
                        session["Logged"]=True
                        session["username_id"]=i
                    i+=1
                    print(session)


                return redirect(url_for('home'))
            else:
                flash("usuario o contrasena incorrecta")
        else:

            flash('Contrasena o usario incorrecto')



    return render_template("login.html",form=formulario,title=title)
@app.route('/home',methods=['GET','POST'])


def home():
    pass
    global usuarios, amigos
    chatsactivos=[]
    i=0


    entries = {'datos1': usuarios[session["username_id"]], 'datos2': session["username_id"], 'datos3': Mensajes[session["username_id"]]}
    formulario = forms.Add(request.form)
    buscarusuario=formulario.username.data
    contador=session["username_id"]
    print()

    if request.method=='POST':


      
        if request.form["uno"]=="Añadir":
            pass            
            if buscarusuario in usuarios and buscarusuario!=usuarios[session["username_id"]]:
                pass

                if buscarusuario in amigos[session["username_id"]]:
                    pass

                    
                else:
                    for datos in usuarios:
                        if datos==buscarusuario:
                            break
                        i+=1
                    print(i)
                    session["chatactivo"]=buscarusuario
                    print(amigos)
                    amigos[i].append("hola")

                    amigos[session["username_id"]].append(buscarusuario)
                    pass
            else:
                pass
                flash("El usuario ingresado es incorrecto")
        print(session["chatactivo"])
        
        if request.form["uno"]=="Enviar" : 
            print("hola")

        else:
            if request.form["uno"]!="Añadir":
                 print("usarioooo")
                 if request.form["uno"]!="Enviar":
                     session["chatactivo"]==request.form["uno"]
                     print(request.form["uno"])
                     print(session["chatactivo"])
            else:
                pass


        

    return render_template("home.html", form=formulario,amigos=amigos,contador=contador,chatsactivos=chatsactivos)
@app.route('/home2',methods=['GET','POST'])


def home2():
    return("hola")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
