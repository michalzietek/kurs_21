from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello/")
def hello():
    return "Hello"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"

@app.route("/magazyn/<name>")
def magazyn(name):
    return render_template("example.html", name=name)

@app.route("/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("main.html")
    elif request.method == "POST":
        mail_adres = request.form.get("adres_email")
        return f"Stworzyles uzytkownika o adresie email: {mail_adres}"
