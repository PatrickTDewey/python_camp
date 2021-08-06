from flask import Flask, render_template, redirect, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "The secret is awesome, you should know"

my_dict = {}

@app.route('/')
def index():
    if 'tries' not in session:
        session['tries'] = int(0)
    elif int(session['tries']) == 15 or int(session['gold'] >= 300):
        if int(session['gold']) >= 300 and int(session['tries']) <= 15:
            session['win/lose'] = 'won'
        else:
            session['win/lose'] = 'lost'
        session['switch'] = True
    if 'gold' not in session:
        session['gold'] = 0
    
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S %p - %d/%m/%Y")
    session['value'] = (request.form['process'])
    if 'message' not in session:
        session['message'] = []

    if session['value'] == 'cave':
        gold_return = random.randint(5, 10)
        session["message"].append(
            f"<ul><li class='green'>Earned {gold_return} golds from the cave on {dt_string}</li></ul>")
        session['gold'] += gold_return
        session['tries'] += 1
    elif session['value'] == 'farm':
        gold_return = random.randint(10, 20)
        session["message"].append(
            f"<ul><li class='green'>Earned {gold_return} golds from the house on {dt_string}</li></ul>")
        session['gold'] += gold_return
        session['tries'] += 1
    elif session['value'] == 'house':
        gold_return = random.randint(2, 5)
        session["message"].append(
            f"<ul><li class='green'>Earned {gold_return} golds from the house on {dt_string}</li></ul>")
        session['gold'] += gold_return
        session['tries'] += 1
    elif session['value'] == 'casino':
        gold_return = random.randint(-50, 50)
        if gold_return < 0:
            session["message"].append(
                f"<ul><li class='red'>Lost {gold_return * -1} golds from the casino on {dt_string}</li></ul>")
            session['gold'] += gold_return
            session['tries'] += 1
        else: 
            session["message"].append(
                f"<ul><li class='green'>Gained {gold_return} golds from the casino on {dt_string}</li></ul>")
            session['gold'] += gold_return
            session['tries'] += 1
    print(session['message'])
    
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear();
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
