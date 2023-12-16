# This API will provide a dictionary meaning of a word when provided
from flask import Flask, render_template
import pandas as pd
FILEPATH = "dictionary.csv"

app = Flask(__name__)

df = pd.read_csv(FILEPATH)


# API Home Page
@app.route("/")
def home():
    return render_template("home.html")


# API request when providing a word in format http://127.0.0.1:5000/api/v1/[word]
@app.route("/api/v1/<word>")
def api(word):

    definition = df.loc[df["word"] == word]['definition'].squeeze()
    results = {"word": word, "definition": definition}

    return results
# Returns the dictionary list from the API - http://127.0.0.1:5000/api/


@app.route("/api/")
def all():
    d = df.to_dict(orient='records')
    return d


if __name__ == "__main__":
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)

    app.run(debug=True, port=5000)
