import os
import json
import random
import string
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

DATA_FILE = os.path.join('data', 'links.json')

def load_links():
    """Reads state safely from the JSON file."""
    if not os.path.exists(DATA_FILE):
        # Create directory and empty structure if they don't exist
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
        return {}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_links(data):
    """Writes updated state back to the JSON file to prevent loss."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def generate_short_code(length=6):
    """Generates a unique 6-character alphanumeric code."""
    links = load_links()
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if code not in links:
            return code

@app.route('/')
def index():
    """Home route showing the shorten form."""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    """Handles form submission with robust URL validation."""
    long_url = request.form.get('long_url', '').strip()
    
    # Validation: Ensure it's not empty and starts with http:// or https://
    if not long_url or not (long_url.startswith('http://') or long_url.startswith('https://')):
        error_msg = "Invalid URL. It must be non-empty and start with http:// or https://"
        return render_template('index.html', error=error_msg, previous_value=long_url)
    
    links = load_links()
    
    # Generate unique short code
    short_code = generate_short_code()
    
    # Save mapping with click count initialized to 0
    links[short_code] = {
        "original_url": long_url,
        "clicks": 0
    }
    save_links(links)
    
    # Construct short link presentation format
    short_link = f"{request.host_url}s/{short_code}"
    return render_template('index.html', short_link=short_link)

@app.route('/s/<code>')
def redirect_to_url(code):
    """Looks up short code, increments counter safely, and redirects."""
    links = load_links()
    
    if code in links:
        # Crucial State Modification: Increment click count and save back immediately
        links[code]["clicks"] += 1
        save_links(links)
        return redirect(links[code]["original_url"])
    
    # Return custom 404 with helpful message if short code doesn't exist
    return render_template('index.html', error="Oops! This shortened code does not exist."), 404

@app.route('/dashboard')
def dashboard():
    """Displays a complete table of all mappings and analytics."""
    links = load_links()
    return render_template('dashboard.html', links=links)

@app.route('/api/links')
def api_links():
    """REST API endpoint returning all links as raw JSON."""
    links = load_links()
    return jsonify(links)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =8080)