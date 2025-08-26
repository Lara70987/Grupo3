import sqlite3
import os

DB_NAME = "banco.db"

def load_data():
    """Carrega todas as notas do banco, ordenando favoritos primeiro"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, favorite FROM note ORDER BY favorite DESC, id ASC")
    rows = cursor.fetchall()
    conn.close()

    notes = []
    for row in rows:
        notes.append({
            "id": row[0],
            "titulo": row[1],
            "detalhes": row[2],
            "favorita": bool(row[3])
        })
    return notes

def load_template(nome_arquivo):
    """Carrega templates HTML"""
    caminho = "templates/" + nome_arquivo
    with open(caminho, 'r', encoding='utf-8') as f:
        html = f.read()
    return html

def armazena_coisas(titulo, detalhes):
    """Salva uma nova nota no banco"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (titulo, detalhes)
    )
    conn.commit()
    conn.close()

def deletar_nota(note_id):
    """Apaga uma nota do banco pelo ID"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

def get_note_by_id(note_id):
    """Retorna uma nota específica pelo ID"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "titulo": row[1],
            "detalhes": row[2]
        }
    return None

def update_note(note_id, titulo, detalhes):
    """Atualiza uma nota existente"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE note SET title = ?, content = ? WHERE id = ?",
        (titulo, detalhes, note_id)
    )
    conn.commit()
    conn.close()

def toggle_favorite(note_id): 
    """Alterna o estado de favorito de uma nota"""
    print(f"Toggling favorite for note ID: {note_id}")  # Log de depuração
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT favorite FROM note WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    
    if row:
        print(f"Current favorite status: {row[0]}")  # Log de depuração
        new_favorite_status = not row[0]
        print(f"New favorite status: {new_favorite_status}")  # Log de depuração
        cursor.execute("UPDATE note SET favorite = ? WHERE id = ?", (new_favorite_status, note_id))
        conn.commit()
        print("Favorite status updated in the database.")  # Log de depuração
    conn.close()
