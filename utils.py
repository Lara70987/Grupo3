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
