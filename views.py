from flask import redirect
from utils import load_data, load_template, armazena_coisas, deletar_nota, get_note_by_id, update_note, toggle_favorite

def index():
    note_template = load_template('components/note.html')
    notes_li = [note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'],favorite_icon='★' if dados['favorita'] else '☆') for dados in load_data()]
    return '\n'.join(notes_li)

def submit(titulo, detalhes):
    armazena_coisas(titulo, detalhes)

def delete(note_id):
    deletar_nota(note_id)


def edit(note_id):
    return get_note_by_id(note_id)

def favorite(note_id):
    """Favorita ou desfavorita uma nota"""
    toggle_favorite(note_id)
    return redirect('/')

def save_edit(note_id, titulo, detalhes):
    update_note(note_id, titulo, detalhes)