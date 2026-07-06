# FLASK URL SHORTENER
A lightweight web application built with Flask and JSON file storage to fulfill all core development specifications for the Tech Track Week 5 Capstone.  
## Live Demo

[![Live Website](https://img.shields.io/badge/Demo-Live%20Website-brightgreen?style=for-the-badge)](https://linkshortener-production-ce89.up.railway.app)

# 🛠️ Features

### URL Shortening:
Generates a unique 6-character alphanumeric code when a long URL is submitted via the frontend form.
### Dynamic Redirection: 
Resolves short codes via /s/<code>, updating click metrics to the file system before redirecting the user.
### State Persistence: 
Increments click counters seamlessly on every redirect and flushes the updated payload straight back to links.json.
### Robust Input Validation: 
Rejects empty fields or strings missing explicit http:// or https:// frameworks.
### Live Analytics Dashboard: 
Renders a clean interface overviewing mapped codes, target URLs, and real-time interaction logs.
### Error Mitigation: 
Catches missing, bad, or expired short tokens through a custom styled 404 Not Found page.

# 📂 Project Structure

### templates/: 
Contains the HTML UI files (base.html for layout inheritance, index.html for the submission form, dashboard.html for metrics, and 404.html for errors).
### app.py: 
The core application engine handling routing, form processing, URL validation, and JSON read/write operations.
### links.json: 
The persistent flat-file database tracking code mappings and analytical click counts.
### requirements.txt & Procfile: 
System configuration and dependency manifests required for smooth cloud environment deployment.

# ⚙️ App Architecture

 **/ (GET)**: Renders the home view interface featuring the link-shortener input form.
**/shorten (POST)**: Captures input payloads, runs validation checks, generates unique tokens, and appends them to the JSON store.
**/s/<code> (GET)**: Dynamically fetches mapping data, increments the interaction counter, updates the file system, and handles the HTTP redirect.
**/dashboard (GET)**: Parses stored historical data logs to generate the analytical dashboard table layout.
**/api/links (GET)**: An optional RESTful JSON endpoint exposing all active tracking information for testing.

# Quick Start

**1. Clone the project**
git clone https://github.com/aryanshende86-lang/link_shortener.git
cd link_shortener

**2. Set up a Virtual Environment**
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

**3. Install Dependecies and Run**
pip install -r requirements.txt
python app.py

**_Open your browser and go to http://127.0.0.1:5000 to test it out!_**

# APPLICATION SCREENSHOTS 

### Main Interface & URL Validation

<img width="1904" height="835" alt="image" src="https://github.com/user-attachments/assets/9a63c614-b66b-497e-9b30-8bbf0c57d20f" />

### Analytics Dashboard

<img width="1900" height="825" alt="image" src="https://github.com/user-attachments/assets/345571e1-2c68-4231-a288-a28ad2136d5f" />

### API

<img width="1920" height="529" alt="image" src="https://github.com/user-attachments/assets/ac61bd13-e03b-46b7-b995-1b721ed7e962" />

# 🌐 Deployment
This application is configured for production and live-deployed using Railway.app.
Continuous Deployment: Any pushes or merges to the main branch trigger automated building blocks handled via the project's root 
Procfile (web: gunicorn app:app).

# AUTHOR
Aryan shende
