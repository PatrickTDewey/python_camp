from dojo_survey_app import app
from flask import render_template, redirect, request, session, flash
from dojo_survey_app.models.dojo import Dojo
# Display Routes
@app.route('/dojos')
def index():
    
    return render_template('index.html')

# Action routes
@app.route('/dojos/create', methods=["POST"])
def create():
    if not Dojo.validate_survey(request.form):
        return redirect('/dojos')
    survey_entry = Dojo.save(request.form)
    print(survey_entry)
    return redirect(f'/dojos/{survey_entry}')

@app.route('/dojos/<int:entry_id>')
def info(entry_id):
    data = {
        'id': entry_id
    }
    entry = Dojo.get_info(data)
    print(entry)
    return render_template("info.html", entry = entry[0])

