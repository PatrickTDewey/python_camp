from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template("index.html")

@app.route('/checkout', methods=['POST', 'GET'])
def get_checkout():
    print('Got Post Info')
    if request.method == 'POST':
       result = request.form
       strawberry = int(result['strawberry'])
       raspberry = int(result['raspberry'])
       apple = int(result['apple'])
    return render_template('checkout.html', form_data = result, strawberry = strawberry, raspberry = raspberry, apple= apple)

@app.route('/checkout')
def checkout_page_route():
    
    return render_template('checkout.html')
# @app.route('/users', methods =['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form['name'], request.form['email'])

#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)