'''
Introduction to Flask project
'''

# Importing the os module from the standard Python library
import os
# Importing the Flask class from the flask module
from flask import Flask

# Creating an instance of the Flask class and storing it in a variable called app
# The first argument of the Flask class is the name of the application’s module - our package
# __name__ is a built-in Python variable. It is needed so that Flask knows where to look for templates, static files
app = Flask(__name__)

@app.route('/')
def index():
    '''
    Returns HTML
    '''
    return '<h1>Hello,</h1> <h2>World<h2>'

# __main__ is the name of the default module in Python
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True)
    