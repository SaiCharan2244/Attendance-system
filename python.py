from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("your-firebase-service-account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    name = data.get('name')
    timestamp = datetime.datetime.now()

    # Add record to Firestore
    doc_ref = db.collection('attendance').document()
    doc_ref.set({
        'name': name,
        'timestamp': timestamp,
        'status': 'present'
    })

    return jsonify({'message': f'Attendance marked for {name}'})

if __name__ == '__main__':
    app.run(debug=True)
