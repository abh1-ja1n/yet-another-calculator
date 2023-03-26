from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app, supports_credentials=True)

# @cross_origin(origins=['http://frontend:3000'])

@app.route('/sqrt', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_square_root():
    data = request.get_json()
    num = float(data['number'])
    
    if num < 0:
        return jsonify({'error': 'Please enter a non-negative number'})
    
    result = math.sqrt(num)
    response = jsonify({'result': result})
    return response

@app.route('/factorial', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_factorial():
    data = request.get_json()
    num = int(data['number'])
    
    if num < 0:
        return jsonify({'error': 'Please enter a non-negative integer'})
    
    result = math.factorial(num)
    response = jsonify({'result': result})
    return response

@app.route('/ln', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_ln():
    data = request.get_json()
    num = float(data['number'])
    
    if num <= 0:
        return jsonify({'error': 'Please enter a positive number'})
    
    result = math.log(num)
    response = jsonify({'result': result})
    return response

@app.route('/power', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_power():
    data = request.get_json()
    num = float(data['number'])
    power = float(data['power'])
    
    if num == 0 and power <= 0:
        return jsonify({'error': 'Cannot raise zero to a non-positive power'})
    
    result = math.pow(num, power)
    response = jsonify({'result': result})
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
