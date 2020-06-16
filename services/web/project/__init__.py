from flask import Flask, jsonify, request
from flask_cors import CORS
from bson import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)
# Settings
CORS(app)
# Database set up
app.config['MONGO_URI'] = 'mongodb://db:27017/dbprod'
mongo = PyMongo(app)

# Database
db = mongo.db.dbprod


@app.route('/', methods=['GET'])
def home():
    data = {'hello': 'world'}
    return jsonify(data)


# Routes
@app.route('/user', methods=['POST'])
def user():
    id = db.insert({
        "name": request.json['name'],
        "email": request.json['email'],
        "password": request.json['password']
    })
    return jsonify(str(ObjectId(id)))


if __name__ == "__main__":
    app.run(debug=False)
