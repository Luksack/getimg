import os

from flask import Flask, request, render_template

from resources import censorship, get_image

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def user_input():
    image_amount = 10
    project_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(project_dir, 'static')
    text = request.form['query']
    try:
        censorship.verify_nice(text)
    except Exception as error:
        return render_template('index.html', er=str(error), bad_results=text)
    else:
        get_image.ImageDownloader(text, image_amount)
        mylist = [f for f in os.listdir(directory) if not f.startswith('.')]
        return render_template('index.html', good_results=text, mylist=mylist)


if __name__ == '__main__':
    app.run(debug=True)
