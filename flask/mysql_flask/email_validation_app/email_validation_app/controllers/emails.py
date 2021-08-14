from email_validation_app import app
from flask import render_template, redirect, request, session, flash
from email_validation_app.models.email import Email

# Display routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/emails')
def show_emails():
    flash(f"success! you entered ({session['email']}), this is a valid email address thank you!")
    all_emails = Email.get_all()
    return render_template("emails.html", all_emails=all_emails)
# Action routes
@app.route('/create', methods=["POST"])
def add_email():
    data = {
        "email_address": request.form['email']
    }
    if not Email.validate_email(data):
        return redirect('/')
    session['email'] = request.form['email']
    email = Email.save(data)
    print(email)
    return redirect('/emails')
