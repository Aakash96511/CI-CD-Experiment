
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My CI/CD Pipeline Project - Version 2</h1>
    <h2>Application is running successfully!</h2>
    <p>Built using Python, Flask and Docker.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Application is healthy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
