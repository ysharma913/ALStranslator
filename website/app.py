from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)

@app.route('/classify', methods=['GET, POST'])
def hello():
    print("GOT TO PYTHON")
    message = request.get_json()
    print(message)
    return jsonify(f'GOT FILENAME OF {message}')  # serialize and use JSON headers
