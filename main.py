from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': "Welcome to the API!"}), 200

@app.route('/about')
def about():
    return jsonify({"version": "0.1", "author": "Alx"}), 200

if __name__ == '__main__':
    app.run(debug=True)