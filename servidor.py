from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print(request.method)
    print(request.headers)

    return render_template('index.html')

@app.route('/processo')
def processo():
    return render_template('processo.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)