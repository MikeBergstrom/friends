from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends2')
@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(created_at, '%b %D') as since, DATE_FORMAT(created_at, '%Y') as year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)