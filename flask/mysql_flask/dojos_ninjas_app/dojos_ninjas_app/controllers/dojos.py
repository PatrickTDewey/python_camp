# users.py
from dojos_ninjas_app import app
from flask import render_template, redirect, request, session, flash
from dojos_ninjas_app.models.dojo import Dojo

# display routes
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)
@app.route('/dojos/<int:dojo_id>')
def dojo_info(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo_info.html", dojo = dojo)
# action routes
@app.route('/dojos/create', methods=["POST"])
def dojo_():
    data = {
        "fname": request.form["dojo_name"]
    }
    dojo = Dojo.save(data)
    return redirect('/dojos')