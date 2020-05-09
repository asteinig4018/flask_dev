from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

note_list = list()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/notes", methods=["GET","POST"])
def notes():
    if request.method == "POST":
        note = request.form.get("note")
        note_list.append(note)
    return render_template("notes.html", note_list = note_list)