from login_reg_app import app
from login_reg_app.models.user import User
from login_reg_app.models.user import bcrypt
from flask import render_template, request, redirect, session, flash


# Display route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/success')
def user_success():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('success.html', user = user)

# Action Routes
@app.route('/users/register', methods=['POST'])
def user_register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pw_length = len(request.form['password'])
    pw_check = bcrypt.check_password_hash(pw_hash, request.form['conf'])
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'email': request.form['email'],
        'pw': pw_hash,
        'pw_check': pw_check,
        'pw_length': pw_length
    }
    # if validation returns is_valid = False, redirect and show messages
    if not User.validate_registration(data): 
        return redirect('/')
    else:
        user_id = User.save(data)
        session['user_id'] = user_id
        return redirect('/users/success')

@app.route('/users/login', methods = ["POST", "GET"])
def user_login():
    if 'user_id' in session:
        return redirect('/users/success')
    elif request.method == "POST":
        data = {
            'email': request.form['email'],
            'pw': request.form['password']
        }
        if not User.validate_login(data):
            return redirect('/users/login')
        else:
            user = User.get_by_email(data)
            session['user_id'] = user.id
            return redirect('/users/success')
    return render_template("login.html")

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/users/login')