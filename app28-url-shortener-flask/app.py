from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Flask!'


if __name__ == "__main__":

    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)
    app.run(debug=True, port=5000)
