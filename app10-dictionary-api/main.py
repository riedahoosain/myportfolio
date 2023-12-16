from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    definition = word.upper()
    results = {"word": word, "definition": definition}
    return results


if __name__ == "__main__":
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    app.run(debug=True, port=80)
