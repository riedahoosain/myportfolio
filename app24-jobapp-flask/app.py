# Job Application Web App using Flask
from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/")
def index():
    """Loads the home page"""
    return render_template("index.html")


if __name__ == "__main__":
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)

    app.run(debug=True, port=5000)