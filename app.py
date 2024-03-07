from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import request

from hublisten import system_msg
from hublisten import client

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index_get(client):
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_post():
    text = request.get_json().get("message")
    response = system_msg(text)
    message = {"answer": response}
    return jsonify(message)