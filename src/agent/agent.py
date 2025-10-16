from mistralai import Mistral
from src.agent.prompts import SYSTEM_PROMPT
from src.agent.memory import criar_memoria
from src.utils.helpers import variar_ritmo, adicionar_metafora, adicionar_interjeicao
from src.tools.sentiment_analysis import analisar_sentimento

class HumanizedAgent:
    def __init__(self, config):
        self.memory = criar_memoria()
        self.client = Mistral(api_key=config["mistral"]["api_key"])
        self.model = config["mistral"]["model"]
        self.temperature = config["mistral"]["temperature"]

    def responder(self, user_input):
        sentimento = analisar_sentimento(user_input)
        
        # Adiciona contexto de sentimento ao prompt
        prompt_contextual = f"{SYSTEM_PROMPT}\n\nUsuário está {sentimento}. Responda de forma empática e criativa.\n\nUsuário: {user_input}"
        
        # Gera resposta usando Mistral AI
        response = self.client.chat.complete(
            model=self.model,
            messages=[{"role": "user", "content": prompt_contextual}],
            temperature=self.temperature
        )
        
        resposta = response.choices[0].message.content
        
        # Aplica humanização
        resposta = variar_ritmo(resposta)
        resposta = adicionar_metafora(resposta, sentimento)
        contexto = "empatia" if sentimento == "negativo" else "pensando"
        resposta = adicionar_interjeicao(resposta, contexto)
        
        return resposta