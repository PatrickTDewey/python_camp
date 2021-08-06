from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "This is a freaking secret key, ok?"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    session['form'] = request.form
    print(session['form'])

    return redirect('/info')

@app.route('/info')
def info():
    
    return render_template("info.html")
if __name__ == "__main__":
    app.run(debug=True)
