import os

from flask import Flask, request, render_template, redirect, url_for

from resources import censorship, get_image

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/search-results')
def search_results():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(project_dir, 'static', 'images')
    mylist = [f for f in os.listdir(directory) if not f.startswith('.')]

    return render_template('search-results.html', mylist=mylist)


@app.route('/', methods=['POST'])
def user_input():
    image_amount = 10
    text = request.form['query']
    try:
        censorship.verify_nice(text)
    except Exception as error:
        return render_template('index.html', er=str(error), bad_results=text)
    else:
        get_image.ImageDownloader(text, image_amount)
        return redirect(url_for('.search_results'))


if __name__ == '__main__':
    app.run(debug=True)
