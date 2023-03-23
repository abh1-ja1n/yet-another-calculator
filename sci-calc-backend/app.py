from flask import Flask, jsonify, request
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

# @cross_origin(origins=['http://frontend:3000'])

@app.route('/sqrt', methods=['POST'])
def calculate_square_root():
    data = request.get_json()
    num = float(data['number'])
    result = math.sqrt(num)
    response = jsonify({'result': result})
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    return response

@app.route('/factorial', methods=['POST'])
# @cross_origin(origins=['http://frontend:3000'])
def calculate_factorial():
    data = request.get_json()
    num = float(data['number'])
    result = math.factorial(num)
    response = jsonify({'result': result})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Credentials', '*')
    return response

@app.route('/ln', methods=['POST'])
# @cross_origin(origins=['http://frontend:3000'])
def calculate_ln():
    data = request.get_json()
    num = float(data['number'])
    result = math.log(num)
    response = jsonify({'result': result})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/power', methods=['POST'])
# @cross_origin(origins=['http://frontend:3000'])
def calculate_power():
    data = request.get_json()
    num = float(data['number'])
    power = float(data['power'])
    result = math.pow(num, power)
    response = jsonify({'result': result})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
