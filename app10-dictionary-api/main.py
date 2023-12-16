from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")



@app.route("/")
def home():
    return render_template("home.html")
    


@app.route("/api/v1/<word>")
def api(word):
    
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    results = {"word": word, "definition": definition}
    
    return results

@app.route("/api/")
def all():
  d = df.to_dict(orient='records')
  return d


if __name__ == "__main__":
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    app.run(debug=True, port=5000)