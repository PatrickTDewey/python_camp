from private_wall_app import app
from private_wall_app.models.user import User
from private_wall_app.models.message import Message
from private_wall_app.models.user import bcrypt

from flask import render_template, request, redirect, session, flash

@app.route('/messages/send', methods =['POST'])
def message_send():
    data = {
        'content': request.form['content'],
        'id': request.form['id2'],
        'sent_by': request.form['id']
    }
    message = Message.save(data)
    return redirect('/users/success')