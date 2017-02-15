from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def about():
    return '<h1>August 04, 1990</h1>'

@app.route('/greeting/<name>')
def greeting(name):
    return '<h1>hello %s</h1>' % name

# @app.route('/sum/<int:sumb1>/<int:sumb2>')
# def sum(sumb1, sumb2):
#     return str(sumb1 + sumb2)
#
# @app.route('/multiply/<int:mul1>/<int:mul2>')
# def sum(mul1, mul2):
#     return str(mul1 * mul2)
#
# @app.route('/subtract/<int:sub1>/<int:sub2>')
# def sum(sub1, sub2):
#     return str(sub1 - sub2)

food = ['chicken', 'pizza', 'salad']

@app.route('/favoritefood')
def favfood():
    return jsonify(food[0])
