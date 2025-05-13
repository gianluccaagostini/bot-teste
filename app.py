from flask import Flask, jsonify, request
from botframework.connector import ConnectorClient  # Exemplo, caso você precise de integração com Teams

app = Flask(__name__)

@app.route("/previsao", methods=["POST"])
def previsao():
    dados = request.json
    # Exemplo de previsão com base no input
    return jsonify({"mensagem": "Previsão de interrupção: 10% de chance de chuva amanhã."})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
