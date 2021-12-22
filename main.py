from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "<h2>Main</h2>"

@app.route('/awards')
def awards():    
    return render_template("awards.html")
    
if __name__ == '__main__':  
    app.run(host='127.0.0.1', port=80, debug=True)

