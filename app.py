from flask import Flask, render_template, request
import sys
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
   return send_from_directory(os.path.join(app.root_path, 'static'), 
   'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/calculate', methods=['POST'])
def calculate():
    c0 = float(request.form['c0'])
    c = float(request.form['c'])
    lam = float(request.form['lam'])
    t = float(request.form['t'])
    dosage = calculate_dosage(c0, c, lam, t)
    return f"Dosage at time {t} is {dosage}"

def calculate_dosage(c0, c, lam, t):
    ln2 = math.log(2)
    return c * lam / ln2 + (c0 - c * lam / ln2) * math.exp(-ln2 / lam * t)

if __name__ == '__main__':
    app.run()
