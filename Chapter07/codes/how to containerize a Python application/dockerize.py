#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

# To the main
@app.route("/")
def hello():
    return render_template('index.html')

# To the about
@app.route("/about")
def open():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)