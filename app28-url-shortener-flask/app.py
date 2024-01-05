from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        print(request.form['code'])
        print(request.form['url'])
        return render_template('your_url.html', code=request.form['code'])

    else:
        return "this is not valid"


if __name__ == "__main__":

    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)
    app.run(debug=True, port=5000)
