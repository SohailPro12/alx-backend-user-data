#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def get_index() -> str:
    """The home
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
