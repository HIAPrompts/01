#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from src.tools.sentiment_analysis import analisar_sentimento
from src.utils.helpers import variar_ritmo, adicionar_metafora, adicionar_interjeicao

def test_agent_demo():
    print("Testando o Agente Humanizado (DEMO - sem API)...")
    print("=" * 60)
    
    try:
        # Simular resposta do agente
        user_input = "oi"
        print(f"Usuario: {user_input}")
        
        # Analisar sentimento
        sentimento = analisar_sentimento(user_input)
        print(f"Sentimento detectado: {sentimento}")
        
        # Resposta simulada baseada no sentimento
        if sentimento == "positivo":
            resposta_base = "Oi! Que alegria te ver por aqui! 😊 Como posso te ajudar hoje?"
        elif sentimento == "negativo":
            resposta_base = "Oi... Sinto que você pode estar passando por um momento difícil. Estou aqui para te ajudar! 💙"
        else:
            resposta_base = "Oi! Tudo bem? Como posso te auxiliar hoje?"
        
        print(f"Resposta base: {resposta_base}")
        
        # Aplicar humanização
        resposta = variar_ritmo(resposta_base)
        resposta = adicionar_metafora(resposta, sentimento)
        contexto = "empatia" if sentimento == "negativo" else "pensando"
        resposta = adicionar_interjeicao(resposta, contexto)
        
        print(f"Agente: {resposta}")
        
        print("\n" + "=" * 60)
        print("DEMO: Esta seria a resposta do agente com uma API key valida!")
        print("Para usar o agente real, configure uma API key valida da Mistral AI.")
        
    except Exception as e:
        print(f"Erro durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_agent_demo()
