# Image Finder

This part of the project is supposed to get user input, find images and download them.

## Installing

To run this project You have newest Python 3.6 and all form requirements file.
```
pip install -r requirements.txt
```
## Running flask

To run flask server go to project location where web.py is:
### On linux:
Setting flask app(best to do all three one by one):
```
export FLASK_APP=web.py
```
Setting devvelopment env:
```
export FLASK_ENV=development
```
Running flask:
```
flask run
```
### On Windows:
Setting flask app(best to do all three one by one):
```
set FLASK_APP=web.py
```
Setting devvelopment env:
```
set FLASK_ENV=development
```
Running flask:
```
flask run
```
## Running tests

In terminal type in:
```
py.test getimg/tests --cov=main
```

