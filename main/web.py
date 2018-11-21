from flask import Flask, request, render_template
from main import censorship, get_image
import os
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def user_input():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    directory = os.path.join(project_dir, 'main', 'static')
    text = request.form['query']
    amount = request.form['amount']
    try:
        censorship.verify_nice(text)
    except Exception as error:
        return render_template('index.html', er=str(error), bad_results=text)
    else:
        get_image.ImageDownloader(text, int(amount))
        mylist = [f for f in os.listdir(directory) if not f.startswith('.')]
        print(mylist)
        return render_template('index.html', good_results=text, mylist=mylist)


if __name__ == '__main__':
    app.run(debug=True)
