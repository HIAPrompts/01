#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from src.agent.agent import HumanizedAgent

def test_agent():
    print("Testando o Agente Humanizado...")
    print("=" * 50)
    
    try:
        # Carregar configuração
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        
        print(f"Configuracao carregada")
        print(f"Modelo: {config['mistral']['model']}")
        print(f"Temperature: {config['mistral']['temperature']}")
        
        # Inicializar o agente
        agente = HumanizedAgent(config)
        print("Agente inicializado com sucesso!")
        
        # Testar com "oi"
        print("\nTestando com mensagem: 'oi'")
        print("-" * 30)
        
        resposta = agente.responder("oi")
        print(f"Usuario: oi")
        # Tratar encoding para Windows
        try:
            print(f"Agente: {resposta}")
        except UnicodeEncodeError:
            # Remover caracteres problemáticos
            resposta_clean = resposta.encode('ascii', 'ignore').decode('ascii')
            print(f"Agente: {resposta_clean}")
        
        print("\nTeste concluido com sucesso!")
        
    except Exception as e:
        print(f"Erro durante o teste: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_agent()
