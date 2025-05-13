from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/previsao", methods=["POST"])
def previsao():
    # Aqui você vai processar a requisição do bot
    dados = request.json
    # Exemplo de previsão com base no input
    return jsonify({"mensagem": "Previsão de interrupção: 10% de chance de chuva amanhã."})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
