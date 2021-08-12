# users.py
from users_app import app
from flask import render_template, redirect, request, session, flash
from users_app.models.user import User

# display routes


@app.route('/users')
def user_all():
    all_users = User.get_all()
    return render_template("users.html", all_users = all_users)

@app.route('/users/new')
def user_new():
    return render_template("user_create.html")

@app.route('/users/<int:user_id>')
def user_info(user_id):
    data = {
        "id": user_id
    }
    user = User.get_info(data)
    return render_template("user_info.html", user = user)

@app.route('/users/<int:user_id>/edit')
def user_edit(user_id):
    return render_template("user_edit.html", user_id = user_id)


# action routes
@app.route('/users/create', methods=["POST"])
def user_create():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    user_id = User.get_by_id(data)
    return redirect(f'/users/{user_id}')
@app.route('/users/update', methods = ["POST"])
def user_update():
    data = {
        "id": request.form['id'],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    edit_user = User.update(data)
    return redirect(f"/users/{data['id']}")

@app.route('/users/<int:user_id>/destroy')
def user_destroy(user_id):
    data = {
        "id": user_id
    }
    destroy_user = User.destroy(data)
    return redirect('/users')
