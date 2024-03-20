from . import app , db 
from .models import Medico
from .models import Paciente
from .models import Consultorio
from .models import Cita
from flask import render_template, request, flash, redirect

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
@app.route("/consultorios")
def get_all_consultorio():
    consultorio = Consultorio.query.all()
    return render_template("consultorios.html", consultorio=consultorio  )

#crear ruta para ver las citas
@app.route("/citas")
def get_all_cita():
    cita = Cita.query.all()
    return render_template("citas.html", cita=cita  )

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
        flash("Medico registrado correctamente")
        return redirect ("/medicos")
    
@app.route("/medicos/update/<int:id>", methods=["POST", "GET"])
def update_medico(id):
    especialidades = [
            "cardiologia", 
            "pediatria",
            "oncologia"
        ]
    medico_update = Medico.query.get(id)
    if (request.method == "GET"):
        return render_template("medico_update.html", 
                           medico_update = medico_update,
                           especialidades = especialidades)
    elif(request.method == "POST"):
        #actualizar el medico, con los datos del form 
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return "medico actualizado"
    
    

@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")

        
#crear ruta traer el paciente por id(get)
@app.route("/pacientes/<int:id>", methods=["POST", "GET"])
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
        flash("Paciente registrado correctamente")
        return redirect ("/pacientes")

        #update paciente

@app.route("/pacientes/update/<int:id>", methods=["POST", "GET"])
def update_paciente(id):
        tipo_sangre = [
            "A+", 
            "O-"
            
        ]
        paciente_update = Paciente.query.get(id)
        if (request.method == "GET"):
            return render_template("paciente_update.html", 
                           paciente_update = paciente_update,
                           tipo_sangre = tipo_sangre)
        elif(request.method == "POST"):
        #actualizar el medico, con los datos del form 
            paciente_update.nombre = request.form["nombre"]
            paciente_update.apellidos = request.form["apellidos"]
            paciente_update.tipo_identificacion = request.form["ti"]
            paciente_update.numero_identificacion = request.form["ni"]
            paciente_update.altura = request.form["al"]
            paciente_update.tipo_sangre = request.form["ts"]
            db.session.commit()
        return "paciente actualizado"
    
    

@app.route("/pacientes/delete/<int:id>")
def delete_paciente(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    return redirect("/pacientes")




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
        flash("Consultorio registrado correctamente")
        return redirect ("/consultorios")
    
    
    

       #update consultorio

@app.route("/consultorios/update/<int:id>", methods=["POST", "GET"])
def update_consultorio(id):
       
        consultorio_update = Consultorio.query.get(id)
        if (request.method == "GET"):
            return render_template("consultorio_update.html", 
                           consultorio_update = consultorio_update
                           )
        elif(request.method == "POST"):
        #actualizar el medico, con los datos del form 
            consultorio_update.numero = request.form["numero"]
            db.session.commit()
        return "consultorio actualizado"
    
    

@app.route("/consultorios/delete/<int:id>")
def delete_consultorio(id):
    consultorio_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    return redirect("/consultorios")



#crear ruta para nueva cita
@app.route("/cita/create", methods = [ 'GET', 'POST' ])
def create_cita():
    #mostrar el formulario: metodo GET
    

        #el usuario ingreso con navegador con http://localhost:5000/citas/create
        
    


#cuando el usuario presiona el boton de guardar 
#los datos del formulario viajan al servidor 
#utilizando el metodo post
    
        #cuando se presiona 'guardar'
        #crear un objeto de tipo paciente
        new_Cita = Cita(fecha = request.form["fecha"],
                            paciente_id = request.form["paciente_id"],
                            medico_id = request.form["medico_id"],
                            Consultorio_id= request.form["Consultorio_id"],
                            valor = request.form["valor"] 
                            )

        #añadirlo a la sesion sqlalchemy
        db.session.add(new_Cita)
        db.session.commit()
        flash("cita registrada correctamente")
        return redirect ("/citas")




      #update cita

@app.route("/citas/update/<int:id>", methods=["POST", "GET"])
def update_cita(id):
       
        cita_update = Cita.query.get(id)
        print(cita_update)
        if(request.method == "GET"):
                 return render_template("cita_update.html", 
                             cita_update = cita_update
                             )
        elif(request.method == "POST"):
             #actualizar la cita , con los datos del form 
                 cita_update.fecha = request.form ["fecha"]
                 cita_update.paciente_id = request.form["paciente_id"]
                 cita_update.medico_id = request.form["medico_id"]
                 cita_update.Consultorio_id = request.form["Consultorio_id"]
                 cita_update.valor = request.form["valor"]
                 db.session.commit()
                 return "cita actualizada"
        
    

@app.route("/citas/delete/<int:id>")
def delete_cita(id):
    cita_delete = Cita.query.get(id)
    db.session.delete(cita_delete)
    db.session.commit()
    return redirect("/citas")
        
        