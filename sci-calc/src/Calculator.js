import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import API_URL from './config.js';


function Calculator() {
  const [number, setNumber] = useState('');
  const [power, setPower] = useState('');
  const [result, setResult] = useState('');

  const calculateSquareRoot = async () => {
    try {
        // console.log('fjsd');
      const response = await axios.post(API_URL + '/sqrt', { number });
      setResult(response.data.result);
      // console.log('sgss00');
    } catch (error) {
      console.error(error);
    }
  };

  const calculateFactorial = async () => {
    try {
      const response = await axios.post(API_URL + '/factorial', { number });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  const calculateNaturalLog = async () => {
    try {
      const response = await axios.post(API_URL + '/ln', { number });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  const calculatePower = async () => {
    try {
      const response = await axios.post(API_URL + '/power', { number, power });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <h1>Scientific Calculator</h1>
      <div>
        <label>Number:</label>
        <input type="number" value={number} onChange={(e) => setNumber(e.target.value)} />
      </div>
      <div>
        <label>Power:</label>
        <input type="number" value={power} onChange={(e) => setPower(e.target.value)} />
      </div>
      <div>
        <button onClick={calculateSquareRoot}>Square Root</button>
        <button onClick={calculateFactorial}>Factorial</button>
        <button onClick={calculateNaturalLog}>Natural Logarithm</button>
        <button onClick={calculatePower}>Power</button>
      </div>
      <div>
        <label>Result:</label>
        <span>{result}</span>
      </div>
    </div>
  );
}

export default Calculator;
