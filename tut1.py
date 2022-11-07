from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def hello():
    return render_template('index.html')

@app.route('/anmol')

def anmol():
    return "Hello World 2"

@app.route('/about')

def about():
    name="prithesh"
    return render_template('about.html',name=name)

app.run(debug=True)