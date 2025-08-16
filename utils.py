import json
import os

def load_data(filename):
    caminho = os.path.join('static', 'data', filename)
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return dados

def load_template(nome_arquivo):
    caminho = os.path.join('static', 'templates', nome_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        html = f.read()
    return html

def armazena_coisas(titulo, detalhes):
    with open("static/data/notes.json", "r") as file:
        notes = json.load(file)
    dicio_novo = {}
    dicio_novo["titulo"] = titulo
    dicio_novo["detalhes"] = detalhes
    notes.append(dicio_novo)
    with open("static/data/notes.json", "w") as file:
        json.dump (notes, file)

 

