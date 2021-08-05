from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index_route():
    print('Index Route')
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print('Got post info')
    print(request.form)
    session['form'] = request.form
    # session['name'] = request.form['name']
    # session['email'] = request.form['email']
    return redirect("/show")


@app.route("/show")
def show_user():
    return render_template("show.html", )


if __name__ == "__main__":
    app.run(debug=True)
