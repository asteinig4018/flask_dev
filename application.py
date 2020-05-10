from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

note_list = list()
unsorted_list = list()
sections = list()

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
        #note_list.append(note)
        section = str(request.form.get("section"))
        if section != "":
            k = get_index(section, sections)
            if k == -1:
                list_len = len(sections)
                sections.append(section)
                note_list.append(list())
                note_list[list_len].append(note)
            else:
                note_list[k].append(note)
        else:
            unsorted_list.append(note)
    return render_template("notes.html", note_list = note_list, sections = sections, unsorted_list = unsorted_list)


def get_index(query, check_list):
    k = -1
    iterator = 0
    for item in check_list:
        if query == item:
            k = iterator
        iterator +=1
    return k