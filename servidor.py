from flask import Flask, request, render_template
from database import Database, Candidato

app = Flask(__name__)
db = Database("dados")

@app.route('/')
def index():
    print(request.method)
    print(request.headers)

    return render_template('index.html')

@app.route('/processo')
def processo():
    return render_template('processo.html')

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