from flask import Flask, request, render_template
from main import censorship

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def user_input():
    text = request.form['example']
    try:
        censorship.verify_nice(text)
    except Exception as error:
        return render_template('index.html', er=str(error), bad_results=text)
    else:
        # Function to collect images here
        return render_template('index.html', good_results=text)


if __name__ == '__main__':
    app.run(debug=True)
