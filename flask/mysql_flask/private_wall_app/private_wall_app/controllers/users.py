from private_wall_app import app
from private_wall_app.models.user import User
from private_wall_app.models.message import Message
from private_wall_app.models.user import bcrypt
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

    other_users = User.get_other_users(data)
    user = User.get_by_id(data)
    user_messages = User.get_user_messages(data)
    return render_template('private_wall.html', user = user, other_users = other_users, user_messages = user_messages)

# Action Routes
@app.route('/users/register', methods=['POST'])
def user_register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pw_length = len(request.form['password'])
    pw_check = bcrypt.check_password_hash(pw_hash, request.form['conf'])
    re = request.form['password']
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'email': request.form['email'],
        'pw': pw_hash,
        'pw_check': pw_check,
        'pw_length': pw_length,
        're': re
    }
    # if validation returns is_valid = False, redirect and show messages
    if not User.validate_registration(data): 
        return redirect('/')
    else:
        user_id = User.save(data)
        # flash('User Successfully Registered', 'success')
        session['user_id'] = user_id
        return redirect('/users/success')

@app.route('/users/login', methods = ["POST"])
def user_login():
    data = {
        'email': request.form['email'],
        'pw': request.form['password']
    }
    if not User.validate_login(data):
        return redirect('/')
    else:
        
        user = User.get_by_email(data)
        session['user_id'] = user.id
        return redirect('/users/success')
    

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/')