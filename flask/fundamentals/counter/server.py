from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "some_secritive_key"


@app.route('/')
def index_route():
    
    if 'count' in session:
        session['count'] += int(1)
    else:
        session['count'] = int(1)
    
    return render_template('index.html')
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    # session.pop('count')
    return redirect('/')

@app.route('/count', methods=['POST'])
def count_route():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/destroy_session')

@app.route('/step', methods=['POST'])
def increment():
    print(request.form['number'])
    if not request.form['number']:
        print(True)
    else:
        session['step'] = request.form['number']
    print(session['step'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)