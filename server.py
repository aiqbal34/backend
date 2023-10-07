from flask import Flask, request
from flask_cors import CORS
import json
import sqlite3
app = Flask(__name__)
CORS(app)

@app.route('/')
def api_call():
    
    connection = sqlite3.connect('workouts.db')
    cursor = connection.cursor()
    successdata = []
    param_value = request.args.get('workout_type')
    print(f'Parameter = {param_value}')
    cursor.execute(f"SELECT * FROM WorkOuts WHERE Type = '{param_value}'")
    for row in cursor.fetchall():
        successdata.append(row)
   # print(successdata)
    return json.dumps(successdata), 200, {'Content-Type': 'application/json'}

@app.route('/login')
def login_call():
    
    connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()

if __name__ == '__main__':
    app.run()
