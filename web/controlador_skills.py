from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_skill(nombre, descripcion, certificacion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO skills(nombre, descripcion, certificacion) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion,certificacion))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un skill", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_skill_a_json(skill):
    d = {}
    d['id'] = skill[0]
    d['nombre'] = skill[1]
    d['descripcion'] = skill[2]
    d['certificacion'] = skill[3]
    return d

def obtener_skills():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, certificacion FROM skills")
            skills = cursor.fetchall()
            skillsjson=[]
            if skills:
                for skill in skills:
                    skillsjson.append(convertir_skill_a_json(skill))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los skills", file=sys.stdout)
        skillsjson=[]
        code=500
    return skillsjson,code

def obtener_skill_por_id(id):
    skilljson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, precio,certificacion FROM skills WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, descripcion, certificacion FROM skills WHERE id =" + id)
            skill = cursor.fetchone()
            if skill is not None:
                skilljson = convertir_skill_a_json(skill)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un skill", file=sys.stdout)
        code=500
    return skilljson,code


def eliminar_skill(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM skills WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un skill", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_skill(id, nombre, descripcion, certificacion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE skills SET nombre = %s, descripcion = %s, certificacion=%s WHERE id = %s",
                       (nombre, descripcion, certificacion,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un skill", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
