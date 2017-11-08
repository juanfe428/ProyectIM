from flask import Flask,session
from flask import render_template
from flask import request,url_for,redirect
from flask_wtf import CSRFProtect
from flask import flash

import datetime


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
amigos=[]
Recibidos=[]
Enviados=[]
who="Agrega un usuario para comenzar 😉"

if Enviados==[]:
    a=open("Archivos/len.txt","r")

    texto=a.readlines()
    for numero in texto:
        i=int(numero)
        print(i)
    x=0
    while x!=i:
        amigos.append([])
        Enviados.append([])
        Recibidos.append([])
        x+=1

    a.close()


    f=open("Archivos/amigos.txt","r")
    texto=f.readlines()
    f.close()
    for palabras in texto:
        palabras=palabras.split("/")
        print(palabras)
        for mas in palabras:
            mover=len(mas)
            if mas!="" and mas!="\n":
                print(mas[mover-1])
                index=int(mas[mover-1])
                final=mas.split(mas[mover-1])
                for yafinal in final:
                    if yafinal!="":
                        print(index)
                        print(amigos)
                        amigos[index].append(yafinal)

#Carga los usaurios ya registrados de un archivo texto
f=open("Archivos/usuarios.txt","r")
texto=f.readlines()
f.close()
for palabrasos in texto:
    palabras=palabrasos.split("-")
    for usuario in palabras:
        if usuario!= "":
            usuarios.append(usuario)

#carga las contraseñas de un archivo texto
f=open("Archivos/passwords.txt","r")
texto=f.readlines()
f.close()
for palabrasos in texto:
    palabras=palabrasos.split("-")
    for pswd in palabras:
        if pswd!= "":
            passwords.append(pswd)
print(Enviados)

@app.route('/register', methods=['GET','POST'])


def index():
    global usuarios,passwords,who,amigos,Recibidos,Enviados
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
            f=open("Archivos/usuarios.txt","a")
            f.write(str(usuario)+"-")
            f.close()
            f=open("Archivos/passwords.txt","a")
            f.write(str(password)+"-")
            f.close()
            i=0
            amigos.append([])
            Recibidos.append([])
            Enviados.append([])
            flash("Se ha registrado")
            a=open("Archivos/len.txt","w")

            a.write(str(len(amigos)))
            a.close()


            return redirect(url_for('login_page'))

            
          

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
                session["username"]=usuario


                return redirect(url_for('home'))
            else:
                flash("usuario o contrasena incorrecta")
        else:

            flash('Contrasena o usario incorrecto')



    return render_template("login.html",form=formulario,title=title)
@app.route('/home',methods=['GET','POST'])


def home():
    pass
    global usuarios, amigos,Recibidos,Enviados,who
    now = datetime.datetime.now()
    hora=str(now.hour)+":"+str(now.minute)


    a=open("Archivos/len.txt","r")

    texto=a.readlines()
    for numero in texto:
        i=int(numero)
        print(i)
    x=0
    while x!=i:
        amigos.append([])
        Enviados.append([])
        Recibidos.append([])
        pass
        x+=1


    i=0
    print(Enviados)
    if not Enviados[session["username_id"]]==[]:

        Enviados[session["username_id"]].clear()
    if not Recibidos[session["username_id"]]==[]:

        Recibidos[session["username_id"]].clear()


    print(Enviados[session["username_id"]])


    entries = {'datos1': usuarios[session["username_id"]], 'datos2': session["username_id"]}
    formulario = forms.Add(request.form)
    buscarusuario=formulario.username.data
    contador=session["username_id"]
    if request.method=='POST':

      
        if request.form["uno"]=="Añadir":
            pass            
            if buscarusuario in usuarios and buscarusuario!=usuarios[session["username_id"]]:
                pass

                if buscarusuario in amigos[session["username_id"]]:
                    pass

                    
                else:
                    session["chatactivo"]=buscarusuario
                    print(amigos)
                    who=session["chatactivo"]
                    index1=usuarios.index(buscarusuario)
                    amigos[index1].append(usuarios[session["username_id"]])
                    amigos[session["username_id"]].append(buscarusuario)
                    #Recibidos.pop(session["username_id"])
                    #Enviados.pop(session["username_id"])
                    f=open("Archivos/amigos.txt","a")

                    f.write(str(buscarusuario)+str(session["username_id"])+"/")
                    f.write(str(usuarios[session["username_id"]])+str(index1)+"/")


                    f.close()






                    a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt","w")
                    b=open("Conversaciones/"+str(session["chatactivo"])+"-"+str(session["username"])+".txt","w")


                    a.close()
                    b.close()


                    pass
            else:
                pass
                flash("El usuario ingresado es incorrecto")
        

        
        if request.form["uno"]=="Enviar" and amigos[session["username_id"]]!=[] and request.form["lol"]!="" and session["chatactivo"]!=[]:



            msg=request.form["lol"]
            who=session["chatactivo"]

            a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt","a")
            b=open("Conversaciones/"+str(session["chatactivo"])+"-"+str(session["username"])+".txt","a")            


            #print("a este se envio el mensaje"+str(who))
            #i=usuarios.index(who)
            a.write("-"+str(msg)+"-")
            #Mensaje recibido con indicador/
            b.write("/"+str(msg)+"/")

            a.close()
            b.close()


        else:
            if request.form["uno"]!="Añadir":


                if request.form["uno"]!="Enviar" and amigos[session["username_id"]]!=[]:

                    print("este es el chat activo"+str(request.form["uno"]))
                    session["chatactivo"]=request.form["uno"]
                    who=session["chatactivo"]
                    if not Enviados[session["username_id"]]==[]:

                        Enviados[session["username_id"]].clear()
                    if not Recibidos[session["username_id"]]==[]:

                        Recibidos[session["username_id"]].clear()
                    



        if amigos[session["username_id"]]!=[] and session["chatactivo"]!=[]:
                        
            a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt")

            texto=a.readlines()

            a.close()

            


            for palabras in texto:

                palabras=palabras.split("/")
                for mensajes in palabras:
                    print(mensajes)
                    if not "-" in mensajes:
                        if mensajes!= "\n" and mensajes!=""  :
                            MensajeR=mensajes

                            Recibidos[session["username_id"]].append(MensajeR)
            for palabras in texto:
                palabras=palabras.split("-")
                for mensajes1 in palabras:

                    if "/" in mensajes1:
                        pass
                    else:

                        if mensajes1!= "\n" and mensajes1!="":
                            MensajeE=mensajes1

                            Enviados[session["username_id"]].append(MensajeE)







    
        
    





        

    return render_template("home.html", form=formulario,amigos=amigos,contador=contador,entries=entries,Recibidos=Recibidos,Enviados=Enviados,who=who,hora=hora)
@app.route('/home2',methods=['GET','POST'])


def home2():
    return("hola")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
