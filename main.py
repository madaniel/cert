from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "<h2>Welcome to Daniel Madar Certification Web App</h2>"


@app.route('/awards')
def awards():    
    return render_template("awards.html")
