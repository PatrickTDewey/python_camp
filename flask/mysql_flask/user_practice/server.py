from flask import Flask, render_template, redirect, request
# import the class from user.py
from user import User
app = Flask(__name__)
app.secret_key = "some secretive keys"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def users():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)

    return redirect('/show')
@app.route('/show')
def show():
    users = User.get_all()
    return render_template("users.html", all_users = users)
if __name__ == "__main__":
    app.run(debug=True)