import os
from flask import Flask, flash,redirect, url_for, render_template, request
from datetime import datetime
import psycopg2


app = Flask(__name__)


app.secret_key="Clave-secreta"

#conexion a base de datos



def get_db_connection():
    conn = psycopg2.connect(host='',
                            database='',
                            user='',
                            password='')
    return conn
#context processors
@app.context_processor
def date_now():
    return{
        'now':datetime.utcnow()
    }

@app.route('/')
def index():
    
    edad =101
    personas =['Aldayr', 'Paco','Jose']
    return render_template('index.html',
                            dato1="valor",
                            dato2="valor2",
                            lista =["uno", "dos","tres"],
                            edad=edad,
                            personas=personas
    )


@app.route('/informacion')
@app.route('/informacion/<string:nombre>/')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre = None, apellidos = None):
    texto= ""
    if nombre != None and apellidos != None:
        texto=f"Bienvenido, {nombre} {apellidos}"
    
    return render_template('informacion.html', texto=texto)
    



@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')


@app.route('/crear-coche', methods=['GET','POST'])
def crear_coche():
    if request.method == 'POST':

        marca = request.form['marca']
        modelo= request.form['modelo']
        precio=request.form['precio']
        ciudad=request.form['ciudad']

       
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("INSERT INTO coches (marca, modelo, ciudad, precio) VALUES(%s, %s, %s, %s)",(marca,modelo, ciudad, precio) )
        conn.commit()
        flash('Has creado el coche correctamente')
        return redirect(url_for('index'))
    return render_template('crear_coche.html')


@app.route('/coches')
def coches():
    conn = get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM coches order by id DESC;")
    coches =cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('coches.html', coches=coches)


@app.route('/coche/<coche_id>')
def coche(coche_id):
    conn = get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche =cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('coche.html', coche=coche[0])


@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    conn = get_db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM coches WHERE id = %s", (coche_id))
    conn.commit()
    cursor.close()
    conn.close()
    flash("El coche ha sido eliminado")
    return redirect(url_for('coches'))

@app.route('/editar-coche/<coche_id>', methods=['GET','POST'])
def editar_coche(coche_id):
    if request.method == 'POST':

        marca = request.form['marca']
        modelo= request.form['modelo']
        precio=request.form['precio']
        ciudad=request.form['ciudad']

       
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("""
            UPDATE coches 
            SET marca= %s,
                modelo= %s,
                ciudad= %s,
                precio= %s
            WHERE id=%s
        """,(marca,modelo, ciudad, precio ,coche_id) )

        conn.commit()
        flash('Has editado  el coche correctamente')
        return redirect(url_for('coches'))
    
    conn = get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche =cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('crear_coche.html', coche=coche[0])

if __name__ == '__main__':
    app.run(debug=True)