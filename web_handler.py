from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("display"))

@app.route("/display")
def display():
    db = sqlite3.connect("course.db")
    com = "SELECT * FROM Course"
    result = db.execute(com).fetchall()
    db.close()
    return render_template("display.html", result=result)

@app.route("/newcourse/", methods=["GET", "POST"])
def newcourse():
    if request.method == "POST":
        name = request.form.get("coursename")
        pax = request.form.get("maxpax")
        db = sqlite3.connect("course.db")
        com = "INSERT INTO Course(Name, MaxPax, CurrPax) VALUES ('{}', {}, {})".format(name, pax, 0)
        db.execute(com)
        db.commit()
        db.close()
        return redirect(url_for('display'))
    elif request.method == "GET":
        return render_template("new_course.html")

@app.route("/status/<int:cid>")
def status(cid):
    db = sqlite3.connect("course.db")
    com = "SELECT Client.ID, Client.Email FROM Client, ClientCourse \
        WHERE ClientCourse.ClientID = Client.ID AND ClientCourse.CourseID = {}".format(cid)
    data = db.execute(com).fetchall()
    name = db.execute("SELECT ID, Name FROM Course WHERE ID = {}".format(cid)).fetchone()
    db.close()
    return render_template("status.html", data=data, name=name)

@app.route("/join/<int:cid>", methods=["GET", "POST"])
def join(cid):
    if request.method == "POST":
        db = sqlite3.connect("course.db")
        email = request.form['email'] 
        #unique contraint on email, when record exist, ignore this command
        try:
            db.execute("INSERT INTO Client (Email) VALUES ('{}')".format(email))
        except:
            sqlite3.IntegrityError
        clientid = db.execute("SELECT Client.ID FROM Client WHERE Client.Email='{}'".format(email)).fetchone()
        currpax = db.execute("SELECT CurrPax FROM Course WHERE Course.ID={}".format(cid)).fetchone()
        try:
            db.execute("INSERT INTO ClientCourse VALUES ({}, {})".format(cid, clientid[0]))
        except:
            sqlite3.IntegrityError
            return render_template("join.html", error=1)
        db.execute("UPDATE Course SET CurrPax={} WHERE Course.ID={}".format(currpax[0] + 1, cid))
        db.commit()
        db.close()
        return redirect(url_for("status", cid=cid))
    elif request.method == "GET":
        db = sqlite3.connect("course.db")
        name = db.execute("SELECT Name FROM Course WHERE ID={}".format(cid)).fetchone()
        db.close()
        return render_template("join.html", name=name, error=0)
    
if __name__ == "__main__":
    app.run(debug=True)