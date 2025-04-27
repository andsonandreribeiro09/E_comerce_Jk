from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/contato.html')
def contato():
    return render_template('contato.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
