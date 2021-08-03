from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play_route():
    return render_template("index.html")

@app.route('/play/<int:x>')
def show_number_of_route(x):
    print(x)
    return render_template("index.html", number = x)

@app.route('/play/<int:x>/<string:color>')
def play_number_route(x, color):
    print(x)
    print(color)
    return render_template("index.html", number = x, color = color)
if __name__ == "__main__":
    app.run(debug=True)