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

# CSS customizado para interface mais bonita
css = """
.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.main-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
}

.title {
    text-align: center;
    color: #2d3748;
    font-size: 2.5em;
    font-weight: 700;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.description {
    text-align: center;
    color: #4a5568;
    font-size: 1.2em;
    margin-bottom: 30px;
    font-weight: 400;
}

.input-container, .output-container {
    margin: 20px 0;
}

.input-label, .output-label {
    font-weight: 600;
    color: #2d3748;
    font-size: 1.1em;
    margin-bottom: 10px;
    display: block;
}

.textbox {
    border-radius: 15px !important;
    border: 2px solid #e2e8f0 !important;
    padding: 15px !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    background: #f7fafc !important;
}

.textbox:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    background: white !important;
}

.button {
    border-radius: 25px !important;
    padding: 12px 30px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    text-transform: none !important;
}

.submit-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
}

.submit-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3) !important;
}

.clear-button {
    background: #e2e8f0 !important;
    color: #4a5568 !important;
    border: none !important;
}

.clear-button:hover {
    background: #cbd5e0 !important;
    transform: translateY(-1px) !important;
}

.output-textbox {
    background: #f8fafc !important;
    border: 2px solid #e2e8f0 !important;
    border-radius: 15px !important;
    padding: 20px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    min-height: 200px !important;
}

.footer {
    text-align: center;
    margin-top: 30px;
    color: #718096;
    font-size: 14px;
}
"""

# Criar interface web com design melhorado
with gr.Blocks(css=css, title="🤖 Agente Humanizado") as iface:
    gr.HTML("""
    <div class="main-container">
        <h1 class="title">🤖 Agente Humanizado</h1>
        <p class="description">Converse com um agente que analisa sentimentos, usa metáforas e interjeições naturais!</p>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML('<label class="input-label">💬 Sua mensagem</label>')
            user_input = gr.Textbox(
                lines=3, 
                placeholder="Digite sua mensagem aqui...", 
                label="",
                container=False,
                elem_classes=["textbox"]
            )
            
            with gr.Row():
                clear_btn = gr.Button("🗑️ Limpar", elem_classes=["button", "clear-button"])
                submit_btn = gr.Button("🚀 Enviar", elem_classes=["button", "submit-button"])
        
        with gr.Column(scale=1):
            gr.HTML('<label class="output-label">🤖 Resposta do Agente</label>')
            output = gr.Textbox(
                lines=8,
                label="",
                container=False,
                elem_classes=["output-textbox"],
                interactive=False
            )
    
    gr.HTML("""
        <div class="footer">
            <p>✨ Powered by Mistral AI + LangChain + Gradio</p>
        </div>
    </div>
    """)
    
    # Conectar eventos
    submit_btn.click(
        fn=responder,
        inputs=user_input,
        outputs=output
    )
    
    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=[],
        outputs=[user_input, output]
    )

# Iniciar a interface
if __name__ == "__main__":
    print("Iniciando interface web...")
    print("Acesse: http://localhost:7860")
    iface.launch()