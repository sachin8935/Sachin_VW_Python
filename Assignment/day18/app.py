from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/random-user')
def get_random_user():
    """Fetch random user from RandomUser.me API"""
    try:
        response = requests.get('https://randomuser.me/api/', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()['results'][0]
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/advice')
def get_advice():
    """Fetch random advice from Advice Slip API"""
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()['slip']
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/cat-fact')
def get_cat_fact():
    """Fetch random cat fact from Cat Facts API"""
    try:
        response = requests.get('https://catfact.ninja/fact', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/activity')
def get_activity():
    """Fetch random activity from Bored API"""
    try:
        response = requests.get('https://bored-api.appbrewery.com/random', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/bitcoin-price')
def get_bitcoin_price():
    """Fetch Bitcoin price from CoinGecko API"""
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,inr', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/trivia')
def get_trivia():
    """Fetch random trivia from Open Trivia DB"""
    try:
        response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple', timeout=10)
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()['results'][0]
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
