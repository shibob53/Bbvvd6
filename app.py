from flask import Flask, request, jsonify

app = Flask(__name__)

# The valid key stored on the server
VALID_KEY = "abc123"  # Change this to your actual key

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.get_json()
    key = data.get("key")

    if key == VALID_KEY:
        return jsonify({"status": "valid"}), 200
    else:
        return jsonify({"status": "invalid"}), 401

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
