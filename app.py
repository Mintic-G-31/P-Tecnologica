from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request


app =Flask(__name__)

Lista_usuarios=["Luis","Pedro","Daniel"] 
citas_medicas={
    "001": "actividad 001",
    "002": "actividad 002",
    "003": "actividad 003",
}

sesion_iniciada= False


@app.route("/", methods=["GET"])
@app.route("/inicio", methods=["GET"])
def inicio():
    return render("inicio.html", sesion_iniciada=sesion_iniciada)

@app.route("/Registro", methods=["GET", "POST"])
def registro():
    return "pagina Registro"


@app.route("/ingreso", methods=[ "GET", "POST"])
def ingreso():
   global sesion_iniciada
   if request.method =="GET":
       return render("ingreso.html") 
   else:
       sesion_iniciada= True
       return render("/index.html")

@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada =False

    return redirect("/inicio")

@app.route("/index", methods=["GET","POST"])
def index():
    global sesion_iniciada
    sesion_iniciada =True
    return render("/index.html")


@app.route("/usuario/<id_usuario>", methods=["GET","POST"])
def usuario(id_usuario):
    if id_usuario in Lista_usuarios:
    
       return f"Estas Viendo el Perfil del Usuario:{id_usuario}"
    else:

       return f"Error El Usuario:{id_usuario} no existe"

@app.route("/crear_vuelo", methods=["GET", "POST"])
def crear_notas():
    return "pagina crear_notas"


@app.route("/notas/<id_notas>", methods=["GET" ])
def notas_usuario(id_notas):
    try:
        notas_usuario=int(id_notas)
    except Exception as e:
        id_vuelo = 0     
    if id_notas in notas_usuario:
    
       return f"Estas viendo las notas:{id_vuelo}"
    else:

       return f"Error de nota de usuario:{id_vuelo} no existe" 
    

@app.route("/crear_actividades", methods=["GET", "POST"])
def crear_actividades():
    return "pagina crear actividades de estudiante"

if __name__=="__main__":
    app.run(debug=True)

