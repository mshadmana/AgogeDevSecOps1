import sqlite3
import hashlib
import xml.etree.ElementTree as ET
import pickle
import jwt
import urllib3
from flask import Flask, request
import json  # Added for safe deserialization

# Flask application
app = Flask(__name__)

# 1. **Injection (SQL Injection)**
def get_user_data(user_id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Vulnerable to SQL Injection
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

# 2. **Broken Authentication**
users = {"admin": "password123", "user": "userpass"}

def login(username, password):
    # Insecure login mechanism (plain text password comparison)
    if username in users and users[username] == password:
        # Simulating a token generation without verification
        token = jwt.encode({"user": username}, "secret", algorithm="HS256")
        return f"Logged in, token: {token}"
    else:
        return "Invalid credentials"

# 3. **Sensitive Data Exposure**
def store_password(password):
    # Storing passwords using MD5, which is insecure
    return hashlib.md5(password.encode()).hexdigest()

# 4. **XML External Entities (XXE)**
def parse_xml(xml_string):
    # Vulnerable to XXE attacks
    tree = ET.fromstring(xml_string)
    return tree.find("name").text

# 5. **Broken Access Control**
def delete_user(user_id, current_user):
    # No authorization check: any user can delete any account
    print(f"User {user_id} deleted by {current_user}")

# 6. **Security Misconfiguration**
app.config['DEBUG'] = True  # Debug mode enabled in production (dangerous)

@app.route('/')
def index():
    return "Welcome to the vulnerable app!"

# 7. **Cross-Site Scripting (XSS)**
@app.route('/greet')
def greet():
    name = request.args.get('name')
    # Vulnerable to XSS, input is reflected without validation or sanitization
    return f"Hello, {name}!"

# 8. **Insecure Deserialization**
def insecure_deserialize(data):
    import json  # Import required for safe deserialization
    return json.loads(data)

# 9. **Using Components with Known Vulnerabilities**
def use_vulnerable_library():
    # Using a vulnerable version of urllib3
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://example.com')
    return response.data

# 10. **Insufficient Logging and Monitoring**
@app.route('/admin')
def admin():
    # No logging of access to sensitive areas like admin routes
    return "Welcome to the admin area!"

# Example vulnerable routes
@app.route('/get_user/<user_id>')
def get_user(user_id):
    return str(get_user_data(user_id))

@app.route('/login')
def login_route():
    username = request.args.get('username')
    password = request.args.get('password')
    return login(username, password)

@app.route('/delete_user/<user_id>')
def delete_user_route(user_id):
    current_user = request.args.get('current_user')
    delete_user(user_id, current_user)
    return f"User {user_id} deleted by {current_user}"

@app.route('/store_password/<password>')
def store_password_route(password):
    return store_password(password)

@app.route('/parse_xml', methods=['POST'])
def parse_xml_route():
    xml_string = request.data
    return parse_xml(xml_string)

@app.route('/deserialize', methods=['POST'])
def deserialize_route():
    data = request.data
    return insecure_deserialize(data)

@app.route('/vulnerable_library')
def vulnerable_library_route():
    return use_vulnerable_library()

# Example of vulnerable usage (do not run in production)
if __name__ == '__main__':
    # Example: SQL Injection Exploitation
    get_user_data("1' OR '1'='1")

    # Example: XML External Entities (XXE) Exploitation
    xml_data = '''<?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
    ]>
    <user>
        <name>&xxe;</name>
    </user>
    '''
    parse_xml(xml_data)

    # Example: Insecure Deserialization Exploitation
    payload = b'cos\nsystem\n(S"rm -rf /"\ntR.'  # Dangerous payload
    insecure_deserialize(payload)

    # Running the Flask app
    app.run()

    FAKE_API_KEY= "12345-ABCDE-67890-FGHIJ"