from flask import Flask, request, render_template, redirect
from database import Database, Candidato
from utils import save_data

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/processo', methods=['GET', 'POST'])
def processo():
    if request.method == "GET":
        return render_template('processo.html')
    else:
        form_data = request.form
        save_data(form_data)
        return redirect('/')

@app.route('/time')
def time():
    return render_template('time.html')

@app.route("/nucleos")
def nucleos():
    return render_template('nucleos.html')

@app.route("/fundo")
def fundo():
    return render_template("fundo.html")

@app.route("/parceiros")
def parceiros():
    return render_template("parceiros.html")

@app.route('/aprenda')
def aprenda():
    return render_template("aprenda.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)