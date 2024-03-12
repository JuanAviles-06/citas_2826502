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

#cerar ruta traer el medico por id(get)
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