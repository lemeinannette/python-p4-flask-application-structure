#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5555)

@app.route('/')
def index():
    return'<h1>Welcome to my app !</h1>'
@app.route('/<username>')
def user(username):
    return f'<h1>profile for {username}</h1>'
@app.route('/string:lemein>')
def my_name (lemein):
    return f'<h1>profile for {lemein}</h1>'