import gradio as gr
import yaml
import os
from dotenv import load_dotenv
from src.agent.agent import HumanizedAgent

# Carregar variáveis de ambiente
load_dotenv()

# Carregar configuração
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Usar variáveis de ambiente se disponíveis
if "MISTRAL_API_KEY" in os.environ:
    config["mistral"]["api_key"] = os.environ["MISTRAL_API_KEY"]

# Inicializar o agente
agente = HumanizedAgent(config)

# Função para interagir com o agente
def responder(mensagem):
    try:
        if not mensagem or mensagem.strip() == "":
            return "Por favor, digite uma mensagem para conversar comigo! 😊"
        
        resposta = agente.responder(mensagem)
        return resposta
    except Exception as e:
        return f"Desculpe, ocorreu um erro: {str(e)}. Tente novamente!"

# Criar interface web
iface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(lines=2, placeholder="Digite sua mensagem...", label="Sua mensagem"),
    outputs=gr.Textbox(lines=4, label="Resposta do Agente"),
    title="🤖 Agente Humanizado com Mistral + LangChain",
    description="Converse com um agente que analisa sentimentos, usa metáforas e interjeições naturais!",
    theme="soft",
    allow_flagging="never"  # Remove a necessidade de login
)

# Iniciar a interface
if __name__ == "__main__":
    print("Iniciando interface web...")
    print("Acesse: http://localhost:7860")
    iface.launch()