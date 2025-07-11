import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app, origins="*"
)  # Public consumption since rate limiting by API gateway prevents abuse

VALID_HASH_IDS = [
    "a1b2c3d4e5f6",
    "9876543210ab",
    "fedcba098765",
    "123456789abc",
    "def456789012",
]


@app.route("/verify/<id>")
def verify_hash_id(id):
    """Check if the provided ID exists in the valid hash list"""
    is_valid = id in VALID_HASH_IDS
    return jsonify({"valid": is_valid})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
