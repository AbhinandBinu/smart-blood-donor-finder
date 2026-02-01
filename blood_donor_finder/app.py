
from flask import Flask, render_template, request, redirect, url_for #creates webpp,loads html,get form data,page navigation
from donor import Donor      
from database import DonorDatabase  
from finder import DonorFinder 
from flask import session, flash  #session - admin login ,flash - error messages
from flask import send_file
import webbrowser




import os
from werkzeug.utils import secure_filename

app = Flask(__name__) #creates flask 

app.secret_key = "admin_secret_key"   # required for sessions

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


# ✅ DEFINE upload folder FIRST
UPLOAD_FOLDER = "static/uploads"

# ✅ ENSURE folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True) #creates folder if not exist

db = DonorDatabase() #loads database


@app.route("/") #home page
def index():
    return render_template("index.html", count=len(db.approved())) #pass count of approved donors to html

@app.route("/add", methods=["GET","POST"]) 
def add():
    if request.method == "POST":
        file = request.files["certificate"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        donor = Donor(
            request.form["name"],
            request.form["blood_group"],
            request.form["location"],
            request.form["phone"],
            path
        )
        db.add(donor)
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/search", methods=["GET","POST"])
def search():
    results = []
    if request.method == "POST":
        finder = DonorFinder(db.approved())
        results = finder.search(request.form["blood_group"])
    return render_template("search.html", results=results)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    if request.method == "POST":
        donor_id = request.form["donor_id"]
        for d in db.donors:
            if d.id == donor_id:
                d.status = "approved"
                break
        db.save()

    return render_template("admin.html", donors=db.pending())

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            flash("Invalid credentials")

    return render_template("admin_login.html")


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin_login"))


@app.route("/download/<path:filepath>")
def download_certificate(filepath):
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    return send_file(filepath, as_attachment=True)



if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)


