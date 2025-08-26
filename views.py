from flask import redirect
from utils import load_data, load_template, armazena_coisas, deletar_nota, get_note_by_id, update_note, toggle_favorite

def index():
    note_template = load_template('components/note.html')
    return '\n'.join(note_template)

