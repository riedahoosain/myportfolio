# Job Application Web App using Flask
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


# Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    """Loads the home page"""
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)
    app.run(debug=True, port=5000)
