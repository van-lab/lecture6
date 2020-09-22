from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

texts = ["First: Lorem ipsum dolor sit voluptates?",
"second: fdakd v adfaiejkwqekqlvadfiqjeksf",
"third: fdakdif jfkdafioqeieka 1341 kfdajfd90fa "]

@app.route("/first")
def first():
  return texts[0]

@app.route("/second")
def second():
  return texts[1]

@app.route("/third")
def third():
  return texts[2]
