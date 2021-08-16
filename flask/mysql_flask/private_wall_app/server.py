from private_wall_app import app
from private_wall_app.controllers import users
from private_wall_app.controllers import messages

if __name__=='__main__':
    app.run(debug=True)