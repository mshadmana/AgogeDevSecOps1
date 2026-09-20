#!/usr/bin/env python3
"""
Vulnerable Flask Application - For Educational Purposes Only
This application contains intentional security vulnerabilities.
"""

from flask import Flask, request, render_template_string
import os
import subprocess
import sqlite3
import yaml

app = Flask(__name__)

# Vulnerability 1: Hardcoded credentials
DATABASE_PASSWORD = "super_secret_password_123"
API_KEY = "sk-1234567890abcdef"

# Vulnerability 2: SQL Injection
def get_user(username):
    """Vulnerable to SQL injection attacks."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# Vulnerability 3: Command Injection
@app.route('/ping')
def ping():
    """Vulnerable to command injection."""
    host = request.args.get('host', 'localhost')
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result

# Vulnerability 4: Server-Side Template Injection
@app.route('/greet')
def greet():
    """Vulnerable to SSTI attacks."""
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

# Vulnerability 5: Insecure Deserialization
@app.route('/load_config')
def load_config():
    """Vulnerable to YAML deserialization attacks."""
    config_data = request.args.get('config', '{}')
    config = yaml.load(config_data, Loader=yaml.FullLoader)
    return str(config)

# Vulnerability 6: Path Traversal
@app.route('/read_file')
def read_file():
    """Vulnerable to path traversal attacks."""
    filename = request.args.get('file', 'default.txt')
    with open(f"/app/files/{filename}", 'r') as f:
        return f.read()

if __name__ == '__main__':
    # Vulnerability 7: Debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
