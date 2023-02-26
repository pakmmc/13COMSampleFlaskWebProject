# Import all the functions we might need from flask
from flask import Flask, render_template, request, abort, redirect

# Create the flask app
app = Flask(__name__)

from datetime import datetime

# This is returned when a user goes to '/' (the homepage) in the browser
@app.route('/')
def hello():
    # return redirect("/signup")
    # return "<h1>Hello World!</h1><p>Extra stuff</p>" + "Current time is: " + str( datetime.now() )[11:19]
    return render_template("hello.html",
                           name="World",
                           datetime=datetime,
                           fruits=["apple","banana","pear"])

# This is returned when a user goes to '/test'
@app.route('/test')
def my_function():
    return "It worked!"


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        print(request.form["first_name"])
    
    return render_template('signup_form.html', request=request)


# A user can try to get the /login page either with GET or with POST.
@app.route("/login", methods=["GET", "POST"])
def login():
    # When the form is submitted, the method used to fetch the page will be 'POST'.
    # That means we can check the submitted form fields.
    if request.method == "POST":
        if request.form["password"] == "13COMiscool!":
            return "Yay! you got the password right"
        else:
            return "You got it wrong!", 405
    # If the method is not POST, it will be GET,
    # and in this case we render the form itself.
    else:
        return render_template("login.html")


# This page displays a different user based on what 'id' it is passed.
@app.route("/user", methods=["GET", "POST"])
def user():
    # How dictionaries work:
    # Basically, they are lists but with anything as the key.

    fruit_list = ["banana", "apple", "orange"]
    orint( fruit_list[1] )

    for fruit in fruit_list:
        print(fruit)

    fruit_dict = { "banana": "yellow", "apple": "red", "orange": "orange" }
    print( fruit_dict["apple"] )

    if "banana" in fruit_dict:
        print("Yes, there is a banana in the list")

    # Here is a list of users
    details_list = [
        {
            "first_name": "Mr",
            "last_name": "McLeod",
            "email": "mmc@pak.school.nz"
        },
        {
            "first_name": "Peter",
            "last_name": "He",
            "email": "pethe@pak.school.nz"
        },
        {
            "first_name": "Xiaoyu",
            "last_name": "Sun",
            "email": "xiasun@pak.school.nz"
        },
    ]

    # If the form has been POSTed and 'id' is one of the fields submitted,
    # pick the user with that 'id' and render the template with those details.
    if "id" in request.form:
        id = int(request.form["id"])
        details = details_list[id]
        return render_template("user.html", details=details)
    # Otherwise, render the form.
    else:
        return render_template("user_select.html")


# Whenever the flask server responds with a 404 status code,
# it will run this function.
@app.errorhandler(404)
def not_found(err):
    return "We couldn't find that page!"


# This 'if'-statement checks if this is the main file or
# if it has been imported by another file.
# The idea is, if it has been imported, we probably want to
# run the flask server in the other file, and not in this one.
if __name__ == '__main__':
    # This is some Visual Studio template code so that the app will
    # start on a different 'port' each time it is run with the play button.
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    # This line is actually important, it is the one that starts the flask server.
    app.run(HOST, PORT, debug=True)
