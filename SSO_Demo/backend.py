from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt, datetime

app = Flask(__name__)
CORS(app)
SECRET_KEY = "MySuperSecretKey"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    token = jwt.encode(
        {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        SECRET_KEY, algorithm="HS256"
    )
    return jsonify({"access_token": token})

if __name__ == "__main__":
    app.run(port=5000)
