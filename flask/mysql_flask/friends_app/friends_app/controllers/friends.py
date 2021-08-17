from friends_app import app
from friends_app.models.friendship import Friendship
from flask import redirect, render_template, flash, request, session


@app.route('/friends/create', methods=['POST'])
def create_friend():
    if 'user_id' not in session:
        redirect('/')
    data = {
        'user_id': session['user_id'],
        'friend_id': request.form['friend']
    }
    friend_id = Friendship.save(data)
    return redirect('/users/dashboard')