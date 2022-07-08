from flask import Flask

app == Flask(__name__)
@app.route('/welcome')
def message1():
    return "welcome"
@app.route('/welcome/back')
def message2():
    return "welcome back"
@app.route('/welcome/home')
def message3():
    return "welcome home"
