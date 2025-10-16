import gradio as gr
import yaml
from src.agent.agent import HumanizedAgent

# Carregar configuração
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Inicializar o agente
agente = HumanizedAgent(config)

# Função para interagir com o agente
def responder(mensagem):
    return agente.responder(mensagem)

# Criar interface web
iface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(lines=2, placeholder="Digite sua mensagem..."),
    outputs="text",
    title="🤖 Agente Humanizado com Mistral + LangChain",
    description="Converse com um agente que analisa sentimentos, usa metáforas e interjeições naturais!",
    theme="soft"
)

# Iniciar a interface
if __name__ == "__main__":
    print("Iniciando interface web...")
    print("Acesse: http://localhost:7860")
    iface.launch()
