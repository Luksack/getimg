from flask import Flask, request, render_template
from main import censorship

app = Flask(__name__)


@app.route('/')
def home_page():
    test_var = 'This is a test var to be displayed on page'
    return render_template('index.html', var=test_var)


@app.route('/', methods=['POST'])
def user_input():
    text = request.form['example']
    try:
        censorship.verify_nice(text)
    except Exception as error:
        return str(error)
    else:
        return 'Good word: next function'


if __name__ == '__main__':
    app.run(debug=True)
