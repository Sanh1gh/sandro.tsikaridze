from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/add_task')
def add_task():
    return render_template("add_task.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)