from flask import Flask, render_template, redirect, request
# import the class from user.py
from user import User
app = Flask(__name__)
app.secret_key = "some secretive keys"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def users():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)

    return redirect('/users')
@app.route('/users')
def show():
    users = User.get_all()
    return render_template("users.html", all_users = users)

@app.route('/users/<int:x>')
def show_user(x):
    data = {
        "id": x
    }
    user = User.show(data)
    return render_template("user.html", user = user)

@app.route('/users/<int:x>/edit')
def edit(x):
    return render_template("edit.html", x = x)

@app.route('/update', methods = ['POST'])
def update():
    data = {
        "id": request.form['id'],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    edit_user = User.update(data)
    return redirect('/users')

@app.route('/users/<int:x>/destroy')
def destroy(x):
    data = {
        "id": x
    }
    destroy_user = User.destroy(data)
    return redirect('/users')
if __name__ == "__main__":
    app.run(debug=True)