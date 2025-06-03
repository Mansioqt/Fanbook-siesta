import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Get MongoDB URI and Database name from environment variables
MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/homework', methods=['GET'])
def homework_get():
    articles = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'articles': articles})

@app.route('/homework', methods=['POST'])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.fanmessages.insert_one(doc)
    return jsonify({'msg': 'Upload complete!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) 
#Nama:Lukman Sucipto
#Kelas: XI TKJ 3
#Absen:12
