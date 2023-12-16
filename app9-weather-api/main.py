from flask import Flask, render_template

app = Flask("My Website")

@app.route("/")
def mainpage():
    return render_template("home.html")

@app.route("/about")
def about1():
    return render_template("about.html")

@app.route("/about/")
def about2():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

app.run(debug=True)