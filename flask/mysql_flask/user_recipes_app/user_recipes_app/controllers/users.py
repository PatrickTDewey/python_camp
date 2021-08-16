from user_recipes_app import app
from ..models.user import User, bcrypt
from ..models.recipe import Recipe
from flask import render_template, request, redirect, session, flash


# Display route
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/users/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    recipes = Recipe.get_other_recipes(data)
    
    return render_template('dashboard.html', user = user, recipes = recipes)

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
        return redirect('/users/dashboard')

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
        return redirect('/users/dashboard',)
    

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/')