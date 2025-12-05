import os
os.system("python alice.py")

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/iniciar")
def iniciar():
    print("A página foi aberta!")
    return "Flask recebeu a chamada"
