from flask import request, session
import json
import decimal
from __main__ import app
import controlador_skills

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/skills",methods=["GET"])
def skills():
    skills,code= controlador_skills.obtener_skills()
    return json.dumps(skills, cls = Encoder),code

@app.route("/skill/<id>",methods=["GET"])
def skill_por_id(id):
    skill,code = controlador_skills.obtener_skill_por_id(id)
    return json.dumps(skill, cls = Encoder),code

@app.route("/skills",methods=["POST"])
def guardar_skill():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        skill_json = request.json
        ret,code=controlador_skills.insertar_skill(skill_json["nombre"], skill_json["descripcion"], skill_json["certificacion"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/skills/<id>", methods=["DELETE"])
def eliminar_skill(id):
    ret,code=controlador_skills.eliminar_skill(id)
    return json.dumps(ret), code

@app.route("/skills", methods=["PUT"])
def actualizar_skill():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        skill_json = request.json
        ret,code=controlador_skills.actualizar_skill(skill_json["id"],skill_json["nombre"], skill_json["descripcion"], skill_json["certificacion"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code