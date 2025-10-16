from langchain.llms import Mistral
from langchain.chains import LLMChain
from src.agent.prompts import SYSTEM_PROMPT
from src.agent.memory import criar_memoria
from src.utils.helpers import variar_ritmo
from src.tools.sentiment_analysis import analisar_sentimento

class HumanizedAgent:
    def __init__(self, config):
        self.memory = criar_memoria()
        self.llm = Mistral(
            api_key=config["mistral"]["api_key"],
            model=config["mistral"]["model"],
            temperature=config["mistral"]["temperature"]
        )
        self.chain = LLMChain(
            llm=self.llm,
            prompt=SYSTEM_PROMPT,
            memory=self.memory
        )

    def responder(self, user_input):
        sentimento = analisar_sentimento(user_input)
        prompt = f"Usuário está {sentimento}. Responda de forma empática e criativa."
        resposta = self.chain.run(user_input)
        return variar_ritmo(resposta)  # Aplica formatação orgânica
