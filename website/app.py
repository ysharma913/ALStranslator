from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from classifier import classify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Access-Control-Allow-Origin: *"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def hello():
    message = request.get_json()
    print(message["fileName"])
    response = jsonify(f'GOT FILENAME OF {message}')
    response.headers.add("Access-Control-Allow-Origin:  ", "*")

    prediction = classify("../snapshots/" + str(message["fileName"]))
    print(prediction)
    return jsonify(prediction)  # serialize and use JSON headers

if __name__ == "__main__":
    app.run(debug=True, port=9000)
