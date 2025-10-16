import yaml
import sys
from src.agent.agent import HumanizedAgent

def main():
    try:
        # Carrega configuração
        with open("config/config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        # Verifica se a chave foi configurada
        if config["mistral"]["api_key"] == "sua_chave_aqui":
            print("ERRO: Configure sua chave da Mistral no arquivo config/config.yaml")
            print("Substitua 'sua_chave_aqui' pela sua chave real da Mistral AI")
            return
        
        # Inicializa o agente
        print("Inicializando Agente Humanizado...")
        agente = HumanizedAgent(config)
        print("Agente pronto! Digite 'sair' para encerrar.\n")
        
        # Loop de conversa
        while True:
            try:
                user_input = input("Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit']:
                    print("Até logo! 👋")
                    break
                
                if user_input.strip():
                    print("Agente: ", end="", flush=True)
                    resposta = agente.responder(user_input)
                    print(resposta)
                    print()  # Linha em branco para separar
                    
            except KeyboardInterrupt:
                print("\n\nAté logo! 👋")
                break
            except Exception as e:
                print(f"Erro: {e}")
                
    except FileNotFoundError:
        print("ERRO: Arquivo config/config.yaml não encontrado!")
    except Exception as e:
        print(f"Erro ao inicializar: {e}")

if __name__ == "__main__":
    main()
