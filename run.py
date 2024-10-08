'''
Introduction to Flask project
'''

# Importing the os module from the standard Python library

import os
# Importing the Flask class from the flask module

import json
# Importing the json module from the standard Python library

from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

# Creating an instance of the Flask class and storing it in a variable called app
# The first argument of the Flask class is the name of the application’s module - our package
# __name__ is a built-in Python variable. It is needed so that Flask knows where to look
# for templates and static files.
# render_template is a function that comes with the Flask class. It allows you to use
# HTML files in your Python code.

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def index(): # View to be called by the Jinja function for the index/home page
    '''
    Returns the home page
    '''
    return render_template('index.html')


@app.route('/about')
def about(): # View to be called by the Jinja function for the about page
    '''
    Returns the about page
    '''
    data = []
    with open("data/company.json", "r", encoding='utf-8') as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title='About', company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    '''
    Returns info based on the url key
    '''
    member = {}
    with open("data/company.json", "r", encoding='utf-8') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template('member.html', member=member)


@app.route('/contact', methods=["GET", "POST"])
def contact(): # View to be called by the Jinja function for the contact page
    '''
    Returns the contact page
    '''
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form.get("name")))
        # print(request.form.get("name"))
        # print(request.form["email"]) # This is a more streamlined version of the above
    return render_template('contact.html', page_title='Contact')


@app.route('/careers')
def careers():
    '''
    Returns the careers page
    '''
    return render_template('careers.html', page_title='Careers')


if __name__ == '__main__': # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)
