from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import MessageActivity
import requests

class TestBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Captura a mensagem do usuário
        mensagem = turn_context.activity.text.strip().lower()
        if "previsao" in mensagem:
            # Enviar a solicitação para a API Python
            resposta = requests.post("http://127.0.0.1:5000/previsao", json={"input": "Qual a previsão para amanhã?"})
            dados = resposta.json()
            await turn_context.send_activity(MessageActivity(text=dados['mensagem']))
        else:
            await turn_context.send_activity("Desculpe, não entendi sua solicitação.")
