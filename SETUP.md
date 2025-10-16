# 🔧 Configuração do Agente Humanizado

## ⚠️ IMPORTANTE: Configurar API Key

Para o agente funcionar, você precisa configurar a API key da Mistral AI:

### 1. Obter API Key
- Acesse: https://console.mistral.ai/
- Crie uma conta ou faça login
- Gere uma nova API key

### 2. Configurar no Hugging Face
1. Vá para: https://huggingface.co/spaces/AngeloHIA/01/settings
2. Clique em "Variables and secrets"
3. Adicione uma nova variável:
   - **Nome**: `MISTRAL_API_KEY`
   - **Valor**: Sua chave real da Mistral AI
4. Salve as configurações

### 3. Reiniciar o Space
- Após configurar a API key, o Space será reiniciado automaticamente
- Aguarde alguns minutos para o deploy

## 🧪 Testando o Agente

### Teste Local (com API key válida):
```bash
python test_simple.py
```

### Demo (sem API key):
```bash
python test_demo.py
```

## 📱 Acessar a Interface Web

Após configurar a API key, acesse:
https://huggingface.co/spaces/AngeloHIA/01

## 🔍 Solução de Problemas

### Erro 401 Unauthorized:
- Verifique se a API key está correta
- Confirme se a chave tem permissões ativas
- Gere uma nova chave se necessário

### Space não carrega:
- Verifique os logs na aba "Logs"
- Aguarde o processamento das dependências
- Reinicie o Space se necessário

## ✨ Funcionalidades

- ✅ Análise de sentimento
- ✅ Metáforas contextuais
- ✅ Interjeições naturais
- ✅ Interface Gradio moderna
- ✅ Memória conversacional
