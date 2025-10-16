import yaml
from src.agent.agent import HumanizedAgent

def test_agent():
    # Configuração de teste
    config = {
        "mistral": {
            "api_key": "test_key",  # Substitua pela sua chave real
            "model": "mistral-large-latest",
            "temperature": 0.7
        }
    }
    
    try:
        agente = HumanizedAgent(config)
        
        # Teste com diferentes sentimentos
        test_inputs = [
            "Ola! Como voce esta?",
            "Estou muito triste hoje...",
            "Que dia maravilhoso!",
            "Preciso de ajuda com algo"
        ]
        
        print("Testando Agente Humanizado...")
        print("=" * 50)
        
        for i, user_input in enumerate(test_inputs, 1):
            print(f"\nTeste {i}: {user_input}")
            print("-" * 30)
            
            try:
                resposta = agente.responder(user_input)
                print(f"Resposta: {resposta}")
            except Exception as e:
                print(f"Erro: {e}")
                
    except Exception as e:
        print(f"Erro ao inicializar agente: {e}")
        print("\nDica: Configure sua chave da Mistral no config/config.yaml")

if __name__ == "__main__":
    test_agent()