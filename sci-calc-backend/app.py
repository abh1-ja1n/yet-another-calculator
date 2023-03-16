from flask import Flask, jsonify, request
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)
@app.route('/sqrt', methods=['POST'])
def calculate_square_root():
    data = request.get_json()
    num = float(data['number'])
    result = math.sqrt(num)
    return jsonify({'result': result})

@app.route('/factorial', methods=['POST'])
def calculate_factorial():
    data = request.get_json()
    num = float(data['number'])
    result = math.factorial(num)
    return jsonify({'result': result})

@app.route('/ln', methods=['POST'])
def calculate_ln():
    data = request.get_json()
    num = float(data['number'])
    result = math.log(num)
    return jsonify({'result': result})

@app.route('/power', methods=['POST'])
def calculate_power():
    data = request.get_json()
    num = float(data['number'])
    power = float(data['power'])
    result = math.pow(num, power)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
