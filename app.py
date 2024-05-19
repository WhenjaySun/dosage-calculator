from flask import Flask, render_template, request
from calculate_dosage import calculate_dosage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    c0 = float(request.form['c0'])
    c = float(request.form['c'])
    lam = float(request.form['lam'])
    t = float(request.form['t'])
    dosage = calculate_dosage(c0, c, lam, t)
    return f"Dosage at time {t} is {dosage}"

if __name__ == '__main__':
    app.run()
