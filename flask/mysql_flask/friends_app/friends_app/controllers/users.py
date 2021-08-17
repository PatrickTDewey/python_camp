from friends_app import app
from friends_app.models.user import User
from friends_app.models.friendship import Friendship
from flask import request, render_template, redirect, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Display Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    other_users = User.get_potential_friends(data)
    user = User.get_by_id(data)
    all_friends = Friendship.get_all_friends()
    print(all_friends)
    return render_template('dashboard.html', user = user, other_users = other_users, all_friends = all_friends)

# Action Routes
@app.route('/users/register', methods=['POST'])
def user_register():
    if not User.validate_registration(request.form):
        print('Not valid, redirecting...')
        return redirect('/')
    data = {
        'fn': request.form['fn'],
        'ln': request.form['ln'],
        'email':request.form['email'],
        'password': request.form['password'],
        'conf': request.form['conf'],
        'hashed': bcrypt.generate_password_hash(request.form['password'])
    }
    flash('User successfully registered', 'success')
    user_id = User.save(data)
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def user_login():
    data = {
        'email': request.form['email'],
        'pw': request.form['password']
    }
    if not User.validate_login(data):
        print('failed login validation...')
        return redirect('/')
    user = User.get_by_email(data)
    session['user_id'] = user.id
    return redirect('/users/dashboard')

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/')