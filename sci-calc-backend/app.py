import logging
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app, supports_credentials=True)

logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

@app.route('/sqrt', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_square_root():
    data = request.get_json()
    num = float(data['number'])
    logging.info(f'calculate_square_root: input={num}')
    
    if num < 0:
        message = 'Error: Please enter a non-negative number'
        logging.warning(f'calculate_square_root: {message}, input={num}')
        return jsonify({'error': message})
    
    result = math.sqrt(num)
    logging.info(f'calculate_square_root: result={result}')
    response = jsonify({'result': result})
    return response

@app.route('/factorial', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_factorial():
    data = request.get_json()
    num = int(data['number'])
    logging.info(f'calculate_factorial: input={num}')
    
    if num < 0:
        message = 'Error: Please enter a non-negative integer'
        logging.warning(f'calculate_factorial: {message}, input={num}')
        return jsonify({'error': message})
    
    result = math.factorial(num)
    logging.info(f'calculate_factorial: result={result}')
    response = jsonify({'result': result})
    return response

@app.route('/ln', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_ln():
    data = request.get_json()
    num = float(data['number'])
    logging.info(f'calculate_ln: input={num}')
    
    if num <= 0:
        message = 'Error: Please enter a positive number'
        logging.warning(f'calculate_ln: {message}, input={num}')
        return jsonify({'error': message})
    
    result = math.log(num)
    logging.info(f'calculate_ln: result={result}')
    response = jsonify({'result': result})
    return response

@app.route('/power', methods=['POST'])
@cross_origin(supports_credentials=True)
def calculate_power():
    data = request.get_json()
    num = float(data['number'])
    power = float(data['power'])
    logging.info(f'calculate_power: input={num}, power={power}')
    
    if num == 0 and power <= 0:
        message = 'Error: Cannot raise zero to a non-positive power'
        logging.warning(f'calculate_power: {message}, input={num}, power={power}')
        return jsonify({'error': message})
    
    result = math.pow(num, power)
    logging.info(f'calculate_power: result={result}')
    response = jsonify({'result': result})
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
