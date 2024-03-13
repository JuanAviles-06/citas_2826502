from . import app , db 
from .models import Medico
from .models import Paciente
from .models import Consultorio
from .models import Cita
from flask import render_template, request

#crear ruta para ver los medicos 
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html", medicos=medicos  )

#crear ruta para ver los pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html", pacientes=pacientes  )

#crear ruta para ver los consultorios
@app.route("/consultorio")
def get_all_consultorio():
    consultorio = Consultorio.query.all()
    return render_template("consultorio.html", consultorio=consultorio  )

#crear ruta para ver las citas
@app.route("/cita")
def get_all_cita():
    cita = Cita.query.all()
    return render_template("cita.html", cita=cita  )

#crear ruta traer el medico por id(get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html", med = medico)


#crear ruta para nuevo medico 
@app.route("/medicos/create", methods = [ 'GET', 'POST' ])
def create_medico():
    #mostrar el formulario: metodo GET
    if( request.method == 'GET'  ):
        #el usuario ingreso con navegador con http://localhost:5000/medicos/create
        especialidades = [
            "cardiologia", 
            "pediatria",
            "oncologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)
    


#cuando el usuario presiona el boton de guardar 
#los datos del formulario viajan al servidor 
#utilizando el metodo post
    elif(request.method== 'POST'):
        #cuando se presiona 'guardar'
        #crear un objeto de tipo medico 
        new_medico = Medico(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion= request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado" 

        
#crear ruta traer el paciente por id(get)
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html", pac = paciente)


#crear ruta para nuevo paciente
@app.route("/pacientes/create", methods = [ 'GET', 'POST' ])
def create_paciente():
    #mostrar el formulario: metodo GET
    if( request.method == 'GET'  ):
        #el usuario ingreso con navegador con http://localhost:5000/paciente/create
        tipo_sangre = [
            "A+", 
            "O-",
        
        ]
        return render_template("paciente_form.html",
                            tipo_sangre = tipo_sangre)
    


#cuando el usuario presiona el boton de guardar 
#los datos del formulario viajan al servidor 
#utilizando el metodo post
    elif(request.method== 'POST'):
        #cuando se presiona 'guardar'
        #crear un objeto de tipo paciente
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion= request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["ts"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_paciente)
        db.session.commit()
        return "paciente registrado" 




#crear ruta traer el consultorio por id(get)
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html", con = consultorio)


#crear ruta para nuevo consultorio
@app.route("/consultorios/create", methods = [ 'GET', 'POST' ])
def create_consultorio():
    #mostrar el formulario: metodo GET
    if( request.method == 'GET'  ):
        #el usuario ingreso con navegador con http://localhost:5000/consultorio/create
        numero = [
            "512", 
            "410",
            "301"
        ]
        return render_template("consultorio_form.html",
                            numero = numero)
    


#cuando el usuario presiona el boton de guardar 
#los datos del formulario viajan al servidor 
#utilizando el metodo post
    elif(request.method== 'POST'):
        #cuando se presiona 'guardar'
        #crear un objeto de tipo medico 
        new_consultorio = Consultorio(numero = request.form["numero"]
                           
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_consultorio)
        db.session.commit()
        return "consultorio registrado" 