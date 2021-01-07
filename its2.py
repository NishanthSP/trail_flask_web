from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def c():
	render_template('c.html')

