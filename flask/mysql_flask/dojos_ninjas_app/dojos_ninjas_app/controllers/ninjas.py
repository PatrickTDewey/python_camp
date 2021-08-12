# users.py
from dojos_ninjas_app import app
from flask import render_template, redirect, request, session, flash
from dojos_ninjas_app.models.ninja import Ninja
from dojos_ninjas_app.models.dojo import Dojo

# display routes
@app.route('/ninjas')
def ninja_new():
    all_dojos = Dojo.get_all()
    return render_template("ninja_new.html", all_dojos = all_dojos)

# action routes
@app.route('/ninjas/create', methods= ["POST"])
def ninja_create():
    data = {
        'fname': request.form["first_name"],
        'lname': request.form["last_name"],
        'age': request.form["age"],
        'dojo_id': request.form['dojo_id']
    }
    create_ninja = Ninja.save(data)
    return redirect(f"/dojos/{data['dojo_id']}")