from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route("/dojo")
def dojo_route():
    return "Dojo"


@app.route("/say/<string:name>")
def say_hi(name):
    if type(name) == type("string"):
        print(type(name))
        return "Hi " + name
    # else:
    #     return "Error, String not given"

@app.errorhandler(404)
def not_found(error):
    return "Sorry! No response. Try again :)"

@app.route("/repeat/<int:num>/<string:string>")
def num_string_route(num, string):
    num_int = int(num)
    return (string + " ") * num_int
if __name__ == "__main__":
    app.run(debug=True)