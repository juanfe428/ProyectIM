from flask import Flask,session
from flask import render_template
from flask import request,url_for,redirect
from flask import flash
from werkzeug.utils import secure_filename
import datetime
import requests
import os
import forms
import json
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.update(
    DEBUG=False,
    SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT',
    USERNAME="JUAN",
    PASSWORD="ADMIN"
)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




usuarios=[]
passwords=[]
amigos=[]
Mensajes=[]
Solicitudes=[]
Enlinea=[]

who="Agrega un usuario para comenzar 😉"

if Mensajes==[]:
    a=open("Archivos/len.txt","r")

    texto=a.readlines()
    for numero in texto:
        i=int(numero)
    x=0
    while x!=i:
        amigos.append([])
        Solicitudes.append([])
        Mensajes.append([])
        x+=1

    a.close()


    f=open("Archivos/amigos.txt","r")
    texto=f.readlines()
    f.close()
    for palabras in texto:
        palabras=palabras.split("/")
        for mas in palabras:
            mover=len(mas)
            if mas!="" and mas!="\n":
                index=int(mas[mover-1])
                final=mas.split(mas[mover-1])
                amigos[index].append(mas[:-1])

    #Carga de un archivo las solicitudes que tenga cada usuario
    f=open("Archivos/Solicitudes.txt","r")
    texto=f.readlines()
    f.close()
    for palabras in texto:
        palabras=palabras.split("/")
        for mas in palabras:
            mover=len(mas)
            if mas!="" and mas!="\n":
                index=int(mas[mover-1])
                final=mas.split(mas[mover-1])
                Solicitudes[index].append(mas[:-1])

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

@app.route('/register', methods=['GET','POST'])


def index():
    global usuarios,passwords,who,amigos,Mensajes,Solicitudes,Enlinea
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


            Solicitudes.append([])
            flash("Se ha registrado")
            a=open("Archivos/len.txt","w")

            a.write(str(len(amigos)))
            a.close()


            return redirect(url_for('login_page'))

            
          

    return render_template('index.html', title=title, form=formulario)
    

@app.route('/',methods=['GET','POST'])
def login_page():

    global usuarios,passwords

    title = 'Tellme!'

    formulario = forms.LoginForm(request.form)
    usuario=formulario.username.data
    password=formulario.password.data
    if request.method== 'POST' and formulario.validate():

        if usuario in usuarios and password in passwords:

            indice=usuarios.index(usuario)


            if passwords[indice]==password:
            #if usuarios.index(usuario)==passwords.index(password)  :
                i=0
                for user in usuarios:


                    if user==usuario:
                        session["username_id"]=i
                    i+=1
                session["username"]=usuario
                Enlinea.append(usuario)



                return redirect(url_for('home'))
            else:
                flash("usuario o contrasena incorrecta")
        else:

            flash('Contrasena o usario incorrecto')



    return render_template("login.html",form=formulario,title=title)
@app.route('/home',methods=['GET','POST'])


def home():
    pass
    global usuarios, amigos,Mensajes,who,Solicitudes,Enlinea



    Estado=""

    now = datetime.datetime.now()
    hora=str(now.hour)+":"+str(now.minute)
    D = os.path.join(APP_ROOT, "static/img/")
    n=len(Mensajes[session["username_id"]])

    if not Mensajes[session["username_id"]]==[]:

        Mensajes[session["username_id"]].clear()
    


    entries = {'datos1': usuarios[session["username_id"]], 'datos2': session["username_id"]}
    formulario = forms.Add(request.form)
    contador=session["username_id"]

    if request.method=='POST':
    

        if request.form.getlist("tres")!=[]:
            ola=request.form.getlist("tres")
            for el in ola:
                usuarioE=el

            index=session["username_id"]

            f=open("Archivos/Solicitudes.txt","r")

            text=f.read()
            f.close()

            f=open("Archivos/Solicitudes.txt","w")
            borrar=text.replace(str(usuarioE)+str(index)+"/","")
            f.write(borrar)
            f.close()

            Solicitudes[session["username_id"]].remove(usuarioE)
        else:


            if request.form.getlist("dos")!=[]:

                ola=request.form.getlist("dos")
                for el in ola:
                    usuarioA=el
                Solicitudes[session["username_id"]].remove(usuarioA)

                index=session["username_id"]

                f=open("Archivos/Solicitudes.txt","r")

                text=f.read()
                f.close()

                f=open("Archivos/Solicitudes.txt","w")
                borrar=text.replace(str(usuarioA)+str(index)+"/","")
                f.write(borrar)
                f.close()




                session["chatactivo"]=usuarioA
                who=session["chatactivo"]
                if who in Enlinea:
                    Estado="En linea"
                else:
                    Estado="Fuera de linea"
                index1=usuarios.index(usuarioA)
                amigos[index1].append(usuarios[session["username_id"]])
                amigos[session["username_id"]].append(usuarioA)
                a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt","w")
                b=open("Conversaciones/"+str(session["chatactivo"])+"-"+str(session["username"])+".txt","w")
                f=open("Archivos/Amigos.txt","a")
                f.write(str(usuarioA)+str(session["username_id"])+"/")
                f.write(str(usuarios[session["username_id"]])+str(index1)+"/")


                f.close()
                a.close()
                b.close()

            else:
                

          
                if request.form["uno"]=="Añadir" and request.form["buscarusuario"]!="":
                    buscarusuario= request.form["buscarusuario"]
                    pass            
                    if buscarusuario in usuarios and buscarusuario!=usuarios[session["username_id"]]:
                        pass

                        if buscarusuario in amigos[session["username_id"]]:
                            pass
                            flash("El usuario ingresado ya es tu amigo")

                        else:

                            index1=usuarios.index(buscarusuario)

                            if not session["username"] in Solicitudes[index1]:

                                if not session["username"] in Solicitudes[index1]:

                                    Solicitudes[index1].append(usuarios[session["username_id"]])
                                    flash("se ha enviao solicitud a :"+str(buscarusuario))
                                    f=open("Archivos/Solicitudes.txt","a")

                                    f.write(str(usuarios[session["username_id"]])+str(index1)+"/")
                                    f.close()

                            else:
                                flash("Ya se ha enviado solicitud")


                            pass
                    else:
                        pass
                        flash("El usuario ingresado es incorrecto")
                

                
                if request.form["uno"]=="Enviar" and amigos[session["username_id"]]!=[] and request.form["lol"]!="" and session["chatactivo"]!=[]:


                    #Prueba:

                    
                    localizacion = requests.get('http://ip-api.com/json/').json()




                    msg=request.form["lol"]+"   "+"("+str(hora)+"|"+str(localizacion['city'])+")"+"|N|"
                    who=session["chatactivo"]
                    if who in Enlinea:
                        Estado="En linea"
                    else:
                        Estado="Fuera de linea"

                    a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt","a")
                    b=open("Conversaciones/"+str(session["chatactivo"])+"-"+str(session["username"])+".txt","a")            


                    a.write("-"+str(msg)+"-")
                    b.write("/"+str(msg)+"/")

                    a.close()
                    b.close()


                else:

                    if request.form["uno"]=="Enviar2":
                        
                        if 'file' not in request.files:
                            flash('No file part')
                            return redirect(request.url)
                        file = request.files['file']


                            # if user does not select file, browser also
                            # submit a empty part without filename
                        if file.filename == '':
                            flash('No selecionaste ningun archivo(Recarga la Pagina)')
                            return redirect(request.url)
                        if file and allowed_file(file.filename):
                            filename = secure_filename(file.filename)
                                
                            destination = "/".join([D, filename])
                            file.save(destination)
                            print(filename)
                            localizacion = requests.get('http://ip-api.com/json/').json()


                            msg=filename+"|M|"
                            who=session["chatactivo"]
                            if who in Enlinea:
                                Estado="En linea"
                            else:
                                Estado="Fuera de linea"

                            a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt","a")
                            b=open("Conversaciones/"+str(session["chatactivo"])+"-"+str(session["username"])+".txt","a")            
                            a.write("-"+str(msg)+"-")
                            b.write("/"+str(msg)+"/")

                            a.close()
                            b.close()
                    else:

                        if request.form["uno"]=="Salir":
                            Enlinea.remove(session["username"])
                            return redirect(url_for('login_page'))


                        if request.form["uno"]!="Añadir":



                            if request.form["uno"]!="Enviar" and amigos[session["username_id"]]!=[]:

                                session["chatactivo"]=request.form["uno"]
                                who=session["chatactivo"]
                                if who in Enlinea:
                                    Estado="En linea"
                                else:
                                    Estado="Fuera de linea"
                                n=len(Mensajes[session["username_id"]])

                                if not Mensajes[session["username_id"]]==[]:

                                    Mensajes[session["username_id"]].clear()
                                    n=len(Mensajes[session["username_id"]])

                   


                            



                if amigos[session["username_id"]]!=[] and who in amigos[session["username_id"]]:
                                
                    a=open("Conversaciones/"+str(session["username"])+"-"+str(session["chatactivo"])+".txt")

                    texto=a.readlines()

                    a.close()
                    for palabras in texto:
                        palabras=palabras.split("-")
                        for mensajes1 in palabras:

                                                                
                            if "/" in mensajes1 :
                                mensajes1=mensajes1.split("/")
                                for mensajes1 in mensajes1:
                                    if "|M|" in mensajes1:

                                        if mensajes1!= "\n" and mensajes1!=""  :
                                            MensajeR=mensajes1
                                            x=len(MensajeR)-3
                                            Mensajes[session["username_id"]].append(["R",MensajeR[:x],"M"])

                                            pass
                                    else:
                                        if mensajes1!= "\n" and mensajes1!="" :

                                

                                            MensajeR=mensajes1
                                            x=len(MensajeR)-3
                                                                                
                                            Mensajes[session["username_id"]].append(["R",MensajeR[:x],"N"])
                                            pass
                            else:
                                if "|M|" in mensajes1:
                                    if mensajes1!= "\n" and mensajes1!="":
                                        MensajeE=mensajes1
                                        x=len(MensajeE)-3
                                        

                                        Mensajes[session["username_id"]].append(["E",MensajeE[:x],"M"])
                                        pass
                                else:

                                                                    
                                                                    
                                    if mensajes1!= "\n" and mensajes1!="":

                                        MensajeE=mensajes1
                                        x=len(MensajeE)-3
                                                                        
                                        Mensajes[session["username_id"]].append(["E",MensajeE[:x],"N"])
    n=len(Mensajes[session["username_id"]])


    return render_template("home.html", form=formulario,amigos=amigos,contador=contador,entries=entries,Mensajes=Mensajes,who=who,hora=hora,Solicitudes=Solicitudes,n=n,Estado=Estado)
@app.route('/home2',methods=['GET','POST'])


def home2():
    return("hola")

if __name__ == '__main__':
    app.run(debug=True)
