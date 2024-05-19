from flask import Flask, request, jsonify
import sys
import math

app = Flask(__name__)

def calculate_dosage(c0, c, lam, t):
    ln2 = math.log(2)
    return c * lam / ln2 + (c0 - c * lam / ln2) * math.exp(-ln2 / lam * t)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    c0 = float(data['c0'])
    c = float(data['c'])
    lam = float(data['lam'])
    t = float(data['t'])
    dosage = calculate_dosage(c0, c, lam, t)
    return jsonify({'dosage': dosage})

if __name__ == '__main__':
    app.run()