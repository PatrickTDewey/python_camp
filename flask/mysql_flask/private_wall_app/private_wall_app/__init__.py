from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'do not use this key for anything serious'