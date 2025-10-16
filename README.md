---
title: Agente Humanizado com Mistral + LangChain
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
license: mit
python_version: "3.10"
short_description: "Agente conversacional inteligente com análise de sentimento, metáforas e interjeições naturais"
tags:
  - chatbot
  - mistral
  - sentiment-analysis
  - gradio
  - langchain
  - portuguese
---

# 🤖 Agente Humanizado com Mistral + LangChain

Um agente conversacional inteligente que combina análise de sentimento, metáforas criativas e interjeições naturais para criar uma experiência de conversa mais humana e empática.

## ✨ Características

- **Análise de Sentimento**: Detecta automaticamente o estado emocional do usuário
- **Metáforas Dinâmicas**: Adiciona metáforas contextuais baseadas no sentimento
- **Interjeições Naturais**: Inclui interjeições apropriadas para tornar a conversa mais natural
- **Memória Conversacional**: Mantém contexto das conversas anteriores
- **Interface Web Intuitiva**: Interface Gradio moderna e responsiva

## 🚀 Como usar

### Opção 1: Interface Web (Recomendado)
```bash
python app.py
```
Acesse: http://localhost:7860

### Opção 2: Terminal
```bash
python app.py
```

### Opção 3: Demo
```bash
python demo.py
```

## ⚙️ Configuração

1. **Instalar dependências**:
```bash
pip install -r requirements.txt
```

2. **Configurar API Key**:
   - Copie `.env.example` para `.env`
   - Adicione sua chave da Mistral AI
   - Ou configure a variável de ambiente `MISTRAL_API_KEY`

3. **Executar**:
```bash
python app.py
```

## 🏗️ Estrutura do Projeto

```
meu_agente_humanizado/
├── app.py                 # Interface web principal (Gradio)
├── chat.py               # Interface de chat no terminal
├── demo.py               # Demonstração do agente
├── config/
│   └── config.yaml       # Configurações do agente
├── data/
│   └── examples/         # Dados de treinamento
│       ├── interjeicoes.txt
│       └── metaforas.txt
├── src/
│   ├── agent/            # Lógica principal do agente
│   │   ├── agent.py      # Classe principal
│   │   ├── memory.py     # Sistema de memória
│   │   └── prompts.py    # Prompts do sistema
│   ├── tools/            # Ferramentas auxiliares
│   │   ├── sentiment_analysis.py
│   │   └── cultural_references.py
│   └── utils/            # Utilitários
│       └── helpers.py
└── tests/                # Testes unitários
```

## 🔧 Tecnologias Utilizadas

- **Mistral AI**: Modelo de linguagem principal
- **LangChain**: Framework para aplicações LLM
- **Gradio**: Interface web interativa
- **TextBlob**: Análise de sentimento
- **PyYAML**: Configurações

## 📝 Exemplos de Uso

### Conversa Normal
```
Usuário: Olá, como você está?
Agente: Olá! Estou muito bem, obrigado por perguntar! 😊 Como posso te ajudar hoje?
```

### Análise de Sentimento
```
Usuário: Estou triste hoje...
Agente: Sinto muito saber que você está passando por um momento difícil... 💙 Às vezes a vida nos apresenta desafios, mas lembre-se de que você é mais forte do que imagina. Quer conversar sobre o que está te incomodando?
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- Mistral AI pela API de linguagem
- Hugging Face pela plataforma de hospedagem
- Comunidade Python pelos frameworks utilizados