from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "a key about secrets"


@app.route('/')
def index_route():

    class_hidden = 'hidden'
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
        print(session['random'])
    else:
        print(session['random'])

    if 'attempt' not in session:
        session['attempt'] = 0
    return render_template("index.html", class_hidden=class_hidden)


@app.route('/guess', methods=['POST'])
def guess_route():
    session['guess'] = request.form['number']
    if session['guess'] != '':
        if int(session['guess']) == int(session['random']):
            session['response'] = f"Yay, {session['guess']} is the number"
            session['switch'] = True
            session['class_check'] = 'green'
        else:
            if int(session['guess']) > int(session['random']):
                session['response'] = f"Good try, but {session['guess']} is too high"
            else:
                session['response'] = f"Good try, but {session['guess']} is too low"
            session['switch'] = False
            session['class_check'] = 'red'
    else:
        print('Enter number')
    session['attempt'] += 1
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
