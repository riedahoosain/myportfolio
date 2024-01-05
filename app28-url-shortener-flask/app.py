from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        urls[request.form['code']] = {'url':request.form['url']}
        with open("urls.json" ,'w') as url_file:
            json.dump(urls, url_file)

     
        return render_template('your_url.html', code=request.form['code'])

    else:
        return redirect(url_for('home'))


if __name__ == "__main__":

    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    # use host to provide an IP instead
    # app.run(debug=True, host="127.0.0.1", port=5000)
    app.run(debug=True, port=5000)
