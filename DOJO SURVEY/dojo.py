from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="secret info"

@app.route("/")
def index_page():
    return render_template("dojosurvey.html")

@app.route("/survey",methods=["post"])
def survey_page():
    session["user"] = request.form["user"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")

@app.route("/home")
def home_page():
    if "survey" in session:
        del session["survey"]
    return redirect("/")

@app.route("/results")
def result():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)