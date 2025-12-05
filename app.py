from flask import Flask, request, jsonify
from flask_cors import CORS
import alice  # importa teu bot

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Servidor Flask rodando com o chatbot Alice!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pergunta = data.get("mensagem", "")

    resposta = alice.responder(pergunta)  # chama função que você usa no seu bot
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
