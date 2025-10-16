import yaml
from src.agent.agent import HumanizedAgent

def demo_conversas():
    # Carrega configuração
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    print("=== DEMO DO AGENTE HUMANIZADO ===")
    print("Inicializando agente...")
    
    try:
        agente = HumanizedAgent(config)
        print("Agente pronto!\n")
        
        # Conversas de demonstração
        conversas = [
            "Olá! Como você está?",
            "Estou muito triste hoje, perdi meu emprego...",
            "Que dia maravilhoso! Consegui uma promoção!",
            "Preciso de ajuda para estudar programação",
            "Estou ansioso para o final de semana"
        ]
        
        for i, mensagem in enumerate(conversas, 1):
            print(f"--- CONVERSA {i} ---")
            print(f"Você: {mensagem}")
            
            try:
                resposta = agente.responder(mensagem)
                print(f"Agente: {resposta}")
            except Exception as e:
                print(f"Erro na resposta: {e}")
            
            print()
            
    except Exception as e:
        print(f"Erro ao inicializar agente: {e}")

if __name__ == "__main__":
    demo_conversas()
