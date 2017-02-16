from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegitarian, is_gluten_free) VALUES (?, ?, ?, ?, ?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
        connection.commit()
        message = 'Record successfully added'
    except:
        connection.rollback()
        message = 'error in insert operation'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = cursor.execute('SELECT * FROM foods WHERE name = "potato"')
    return query
