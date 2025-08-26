from flask import Flask, render_template, request, redirect
import views

app = Flask(__name__)  # sem template_folder aqui

@app.route('/')
def index():
    notes = views.index()
    return render_template('index.html', notes=notes)

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:note_id>', methods=['GET'])
def delete(note_id):
    views.delete(note_id)
    return redirect('/')

@app.route('/update/<int:note_id>', methods=['GET'])
def edit(note_id):
    nota = views.edit(note_id)
    if nota:
        # aqui você pode chamar só "components/edit.html"
        return render_template('components/edit.html', nota=nota)
    return redirect('/')

@app.route('/update', methods=['POST'])
def save_update():
    note_id = request.form.get('id')
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.save_edit(note_id, titulo, detalhes)
    return redirect('/')

@app.route('/favorite/<int:note_id>', methods=['GET'])
def favorite(note_id):
    views.favorite(note_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
