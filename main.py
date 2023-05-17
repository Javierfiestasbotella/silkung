# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import User, NewTable
from sqlalchemy.orm.exc import NoResultFound
import db
import ejercicios
import errores_archivos as er
import os
from ai import preguntar_chat_gpt
from werkzeug.utils import secure_filename
import datetime
from datetime import date
from flask_mail import Mail, Message
from sqlalchemy.exc import OperationalError
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

mail = Mail(app)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')#PAgina principal
def home():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def enviar_email():
    asunto = request.form['asunto']
    problema = request.form['problema']
    email_usuario = request.form['email_usuario']

    msg = Message(asunto,
                  sender=email_usuario,
                  recipients=['javierfiestasbotella@gmail.com'])
    msg.body = "Correo de usuario {0}: {1}".format(email_usuario, problema)
    mail.send(msg)

    return render_template('user.html')


@app.route('/user_ejercicios')#Ruta donde aparece descripcion de los ejercicios recomendados al alumno
def user_ejercicios():
        username = session['username']
        user = db.session.query(User).filter_by(nombre=username).first()
        #ejercicios_todos = db.session.query(User).filter_by(nombre=username).filter_by(curso=user.curso).first()
        exercices_user = db.session.query(NewTable).filter_by(user_id=user.id_user).first()
        listado=ejercicios.crear_ejercicios(user.curso,exercices_user.lista_ejercicios,)
        return render_template('user_ejercicios.html', user=user, exercices_user=exercices_user, listado=listado)


@app.route('/user_ejercicios_personales/<int:id>')
def user_ejercicios_personales(id):
    usuario = db.session.query(User).filter_by(id_user=id).first()
    user = db.session.query(User).first()
    if user is None:
        return "Usuario no encontrado"
    exercices_user = db.session.query(NewTable).filter_by(user_id=id).first()
    listado = ejercicios.crear_ejercicios(user.curso, exercices_user.lista_ejercicios)
    return render_template('user_ejercicios_personales.html', user=user, exercices_user=exercices_user, listado=listado, usuario=usuario)


@app.route('/alumnos')#ruta hacia la página de los alumnos para el administrador
def alumnos():
    # Obtener todos los usuarios
    usuarios = db.session.query(User).all()

    # Obtener los datos de NewTable para cada usuario
    datos_usuario = {}
    for usuario in usuarios:
        datos_usuario[usuario.id_user] = db.session.query(NewTable).filter_by(user_id=usuario.id_user).all()

    return render_template('alumnos.html', usuarios=usuarios, datos_usuario=datos_usuario)


@app.route('/alumnos_quigong')
def alumnos_quigong():
    # Obtener todos los usuarios de Quigong
    usuarios = db.session.query(User).filter_by(curso='Chikung').all()

    # Obtener los datos de NewTable para cada usuario
    datos_usuario = {}
    for usuario in usuarios:
        datos_usuario[usuario.id_user] = db.session.query(NewTable).filter_by(user_id=usuario.id_user).all()

    return render_template('alumnos.html', usuarios=usuarios, datos_usuario=datos_usuario)


@app.route('/alumnos/pilates')
def alumnos_pilates():
    usuarios = db.session.query(User).filter_by(curso='Pilates').all()
    datos_usuario = {}
    for usuario in usuarios:
        datos_usuario[usuario.id_user] = db.session.query(NewTable).filter_by(user_id=usuario.id_user).all()
    return render_template('alumnos.html', usuarios=usuarios, datos_usuario=datos_usuario)


@app.route('/registro_nuevo')#ruta hacia la página registro Nuevo
def registro_nuevo():
    return render_template('registro_nuevo.html')


@app.route('/registro_nuevo' , methods=['POST'])#ruta hacia la página registro de usuario
def registro_insert():
    nombre_perfil = request.files['img_perfil']
    perfil = nombre_perfil.filename
    nuevo_registro = User(nombre=request.form['nombre'], apellidos=request.form['apellidos'], email=request.form['email'], curso=request.form['curso'], edad=request.form['edad'], perfil=perfil, password=request.form['password'])

    # guardar la imagen
    if 'img_perfil' in request.files:
        img_perfil = request.files['img_perfil']
        if img_perfil.filename != '':
            # generar un nombre seguro para el archivo
            filename = secure_filename(img_perfil.filename)
            # guardar el archivo en la carpeta static
            img_perfil.save(os.path.join(app.static_folder, filename))
            # almacenar la ruta de la imagen en la base de datos
            ruta_perfil = os.path.join('img_perfil', filename)
        else:
            ruta_perfil = None
    else:
        ruta_perfil = None
    db.session.add(nuevo_registro)
    db.session.commit()
    db.session.close()
    return redirect(url_for('alumnos'))


#109510
@app.route('/login')#ruta hacia la página de login
def login():
    return render_template('login.html')


@app.route('/precios')#ruta hacia la página de precios de los cursos
def precios():
    return render_template('precios.html')


@app.route('/videos_ejercicios')#ruta hacia la página de precios de los cursos
def videos_ejercicios():
    return render_template('videos_ejercicios.html')


@app.route('/cv')#ruta hacia la página de precios de los cursos
def cv():
    return render_template('cv.html')


@app.route('/README')#ruta hacia la página de README informacion completa sobre el proyecto
def README():
    return render_template('README.html')


@app.route('/update_user')#ruta hacia la página de login
def update_user():
    return render_template('update_user.html')


@app.route('/horarios')#ruta hacia la página de horarios
def horarios():
    return render_template('horarios.html')


@app.route('/qigong')#ruta hacia la página de informacion de Qigong
def qigong():
    return render_template('informacion_qigong.html')


@app.route('/pilates')#ruta hacia la página de informacion sobre pilates
def pilates():
    return render_template('informacion_pilates.html')


@app.route('/galery_chikung')#ruta hacia la página imagenes de qigong
def galery_chikung():
    return render_template('galery_chikung.html')


@app.route('/galery_pilates')#ruta hacia la página de imagenes de pilates
def galery_pilates():
    return render_template('galery_pilates.html')


@app.route('/peques')#ruta hacia la página de imagenes de los niños
def peques():
    return render_template('peques.html')


@app.route('/editar/<int:id>', methods=['GET'])#get_user(id), toma un parámetro de id como entrada y busca un usuario en la base de datos con ese id. Luego, la función devuelve una plantilla HTML que muestra la información del usuario encontrado.
def get_user(id):
    user = db.session.query(User).get(id)
    return render_template('editar.html', user=user)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    user = db.session.query(User).filter_by(id_user=id).first()
    from_page = request.args.get('from')  # Obtener el valor del parámetro "from"
    if request.method == 'POST':
        user.nombre = request.form['nombre']
        user.apellidos = request.form['apellidos']
        user.edad= request.form['edad']
        user.curso= request.form['curso']
        user.email = request.form['email']
        db.session.commit()

        # Redirigir al usuario a la página correspondiente según el valor del parámetro "from"
        if from_page == 'alumnos':
            return redirect(url_for('alumnos'))
        else:
            return redirect(url_for('user', id=user.id_user))

    else:
        return render_template('editar.html', nombre=user.nombre, user=user, edad=user.edad, email=user.email, apellidos=user.apellidos, curso=user.curso)


@app.route('/form')#ruta a la pagina para rellenar el formulario para crear nuevo login
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST'])#según ponga el login correcto o no va al su usuario o devulve
def haz_login():
    username = request.form['username']
    password = request.form['password']
    user = db.session.query(User).filter_by(nombre=username, password=password).first()
    if user is not None:
        session['username'] = user.nombre
        return redirect(url_for('user'))
    elif username == 'administradora_garcia_cuesta' and password == 'sarayalba':
        return redirect(url_for('alumnos'))
    else:
        return render_template('error.html')


@app.route('/user')
def user():
    if 'username' in session:
        username = session['username']
        user = db.session.query(User).filter_by(nombre=username).first()
        return render_template('user.html', user=user)
        #return redirect(request.referrer)

    else:
        return redirect(url_for('login'))

@app.route('/editar_ejercicios')
def editar_ejercicios():
    today = date.today().strftime('%Y-%m-%d')
    return render_template('editar_ejercicios.html', today=today)


@app.route('/editar_ejercicios', methods=['POST'])
def registro_ejercicios():
    try:
        user_id = request.form['user_id']
        fecha_inicio = datetime.datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        facturas = request.form['facturas']
        lista_ejercicios = request.form['lista_ejercicios']
        cursos = request.form['cursos']

        # Buscar el registro en la tabla por user_id
        registro_existente = db.session.query(NewTable).filter_by(user_id=user_id).first()

        if registro_existente:
            # Si existe, actualizar los campos
            registro_existente.fecha_inicio = fecha_inicio
            registro_existente.facturas = facturas
            registro_existente.lista_ejercicios = lista_ejercicios
            registro_existente.cursos = cursos
        else:
            # Si no existe, crear uno nuevo
            nuevo_registro = NewTable(user_id=user_id, fecha_inicio=fecha_inicio, facturas=facturas,
                                      lista_ejercicios=lista_ejercicios, cursos=cursos)
            db.session.add(nuevo_registro)

        # Confirmar los cambios en la base de datos
        db.session.commit()
        return redirect(url_for('alumnos'))
    except Exception as e:
        db.session.rollback()
        return "Error al guardar los datos: " + str(e)


@app.route('/delete_user')
def index():
    users = db.session.query(User).all()
    return render_template('delete_user.html', users=users)


@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form.get('user_id')

    try:
        user = db.session.query(User).filter_by(id_user=user_id).one()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('alumnos'))
    except OperationalError as e:
        #flash(f"Se produjo un error de tipo {type(e).__name__}: {str(e)}", "error")
        er.crea_fichero(str(e))
        db.session.rollback()

    return redirect(url_for('alumnos'))




@app.route('/chatbot')
def chatbot():
    mensajes = [] # Aquí es donde almacenaremos los mensajes de chat

    # Renderizamos la plantilla chatbot.html y pasamos los mensajes de chat como variable
    return render_template('chatbot.html', mensajes=mensajes)


@app.route('/enviar-mensaje', methods=['POST'])
def enviar_mensaje():
    mensaje = request.form['mensaje']
    fecha = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Enviamos el mensaje del usuario al chatbot y obtenemos la respuesta
    prompt = f'El usuario pregunta: {mensaje}\nChatGPT responde:'
    respuesta = preguntar_chat_gpt(prompt)

    # Almacenamos el mensaje del usuario y la respuesta del chatbot como objetos mensaje
    mensaje_usuario = {'texto': mensaje, 'tipo': 'usuario', 'fecha': fecha}
    mensaje_chatbot = {'texto': respuesta, 'tipo': 'chatbot', 'fecha': fecha}
    mensajes = [mensaje_usuario, mensaje_chatbot]

    # Renderizamos la plantilla chatbot.html y pasamos los mensajes de chat actualizados como variable
    return render_template('chatbot.html', mensajes=mensajes)


@app.route('/edita_desde_admin/<int:id>', methods=['GET', 'POST'])
def edita_desde_admin(id):
    user = db.session.query(User).filter_by(id_user=id).first()
    if request.method == 'POST':
        user.nombre = request.form['nombre']
        user.apellidos = request.form['apellidos']
        user.edad= request.form['edad']
        user.curso= request.form['curso']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('alumnos'))

    else:
        return render_template('edita_desde_admin.html', nombre=user.nombre, user=user, edad=user.edad, email=user.email, apellidos=user.apellidos, curso=user.curso)

@app.route('/formulario_contacto')
def formulario_contacto():
    return render_template('formulario_contacto.html')



@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    asunto = request.form['asunto']
    mensaje = request.form['mensaje']

    # Configurar los detalles del correo electrónico
    remitente = 'javierfiestasbotella@gmail.com'
    destinatario = email
    asunto_correo = asunto
    mensaje_correo = f'Hola {nombre},\n\n{mensaje}'

    # Crear el mensaje de correo electrónico
    mensaje = EmailMessage()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto_correo
    mensaje.set_content(mensaje_correo)

    # Enviar el correo electrónico utilizando SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(remitente, os.getenv('SMTP_PASSWORD'))
        servidor_smtp.send_message(mensaje)

    return 'Correo electrónico enviado con éxito'


if __name__ == '__main__':
    #crear todas las tablas definidas en el modelo de base de datos
    db.Base.metadata.create_all(db.engine)
    #app.run(debug=True)
    try:
        app.run(debug=True)
    except Exception as e:
        er.crea_fichero(str(e))


