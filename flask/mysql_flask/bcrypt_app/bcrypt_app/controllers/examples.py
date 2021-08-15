from bcrypt_app import app
from flask import redirect, request, session, flash, render_template
from bcrypt_app.models.example import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Display Routes
@app.route('/users')
def index():
    if 'user_id' in session:
        print('Session ID: ', session['user_id'])
        return redirect('/users/dashboard')
    return render_template("index.html")

@app.route('/users/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Action Routes
@app.route('/users/create', methods=["POST"])
def user_create():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    check = bcrypt.check_password_hash(pw_hash, request.form['conf'])
    data = {
        "un": request.form['username'],
        "pw": pw_hash,
        'conf': check
    }
    if not User.validate_sign_up(data):
        return redirect('/users')
    else:
        user_id = User.save(data)
        session['user_id'] = user_id
    return redirect('/users')


@app.route('/users/login', methods=["GET","POST"])
def user_login():
    # see if the username provided exists in the database
    if request.method == 'POST':
        
        data = {
            "un": request.form['username'],
            "pw": request.form['password'],
        }
        if not User.validate_login(data):
            return redirect('/users/login')
        else:
            user = User.get_by_un(data)
            session['user_id'] = user.id
            return redirect('/users/dashboard')
            
    elif 'user_id' in session:
        return redirect('/users/dashboard')
    return render_template('login.html')

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/users')