from crypt import methods
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Homepage.html')



if __name__ == "__main__":
    app.run(host="localhost", port = 5000, debug=True)