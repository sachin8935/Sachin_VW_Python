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

@app.route('/api/users')
def get_users():
    """Fetch users from JSONPlaceholder API"""
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
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

@app.route('/api/posts')
def get_posts():
    """Fetch posts from JSONPlaceholder API"""
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json()[:10]
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/random-joke')
def get_random_joke():
    """Fetch a random joke from Official Joke API"""
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
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

@app.route('/api/dog-image')
def get_dog_image():
    """Fetch a random dog image from Dog CEO API"""
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
