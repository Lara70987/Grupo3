from flask import make_response, render_template, redirect
from database import Database, Candidato

db = Database('dados')

def save_data(data):
    print('*'*100)
    print(data)
    print('*'*100)
    
    data_dict = {
        'name': data.get("name"),
        'email': data.get("email"),
        'phone': data.get('phone'),
        'matricula': data.get('matricula'),
        'course': data.get('course'),
        'semester': data.get('semestre')
    }
    cand = Candidato(**data_dict)
    db.add(cand)
    
    return make_response(render_template('index.html'), 303)