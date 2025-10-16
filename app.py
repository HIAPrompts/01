import yaml
from src.agent.agent import HumanizedAgent

def main():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    agente = HumanizedAgent(config)
    while True:
        user_input = input("Você: ")
        resposta = agente.responder(user_input)
        print(f"Agente: {resposta}")

if __name__ == "__main__":
    main()
