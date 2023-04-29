from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def site_m():
    return render_template('index.html')
