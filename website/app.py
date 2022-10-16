from flask import Flask, jsonify, request, render_template
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = "Access-Control-Allow-Origin: *"

@app.route('/')
def index():
    print("RENDERING")
    return render_template('index.html')

@app.route('/classify', methods=['GET, POST'])
def hello():
    print("GOT TO PYTHON")
    message = request.get_json()
    print(message)
    return jsonify(f'GOT FILENAME OF {message}')  # serialize and use JSON headers

if __name__ == "__main__":
    app.run()