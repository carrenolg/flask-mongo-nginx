from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Settings
CORS(app)


@app.route('/', methods=['GET'])
def home():
    data = {'hello': 'world'}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=False)
