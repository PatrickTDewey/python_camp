from flask import Flask

app = Flask(__name__)
app.secret_key = 'do not use this key for anything serious'