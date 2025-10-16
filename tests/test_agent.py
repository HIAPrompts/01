import unittest
from src.agent.agent import HumanizedAgent

class TestHumanizedAgent(unittest.TestCase):
    def test_resposta_nao_vazia(self):
        agente = HumanizedAgent({"mistral": {"api_key": "teste", "model": "teste", "temperature": 0.7}})
        resposta = agente.responder("Olá!")
        self.assertTrue(len(resposta) > 0)

if __name__ == "__main__":
    unittest.main()
