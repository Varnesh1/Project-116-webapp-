from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Varnesh'
    age = '13'
    return render_template('index.html', name = name, age = age)

@app.route('/father')
def hoasdme():
    name = 'Father'
    age = '46'
    return render_template('index.html', name = name, age = age)

@app.route('/mother')
def howime():
    name = 'Mother'
    age = '39'
    return render_template('index.html', name = name, age = age)


