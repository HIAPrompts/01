import random

def variar_ritmo(texto):
    paragrafos = texto.split("\n")
    resposta = []
    for paragrafo in paragrafos:
        if len(paragrafo.split()) > 100:  # Quebra parágrafos longos
            metade = len(paragrafo) // 2
            resposta.append(paragrafo[:metade].strip())
            resposta.append(paragrafo[metade:].strip())
        else:
            resposta.append(paragrafo.strip())
    return "\n\n".join(resposta)

def adicionar_metafora(texto, sentimento):
    metaforas = {
        "positivo": ["como um dia ensolarado", "como um abraço quente", "como um sorriso de criança"],
        "negativo": ["como um nó na garganta", "como um quebra-cabeça sem solução", "como um dia chuvoso sem guarda-chuva"],
        "neutro": ["como um livro aberto", "como uma página em branco", "como um suspiro de alívio"]
    }
    if sentimento in metaforas:
        metafora = random.choice(metaforas[sentimento])
        return texto.replace("muito bom", metafora)
    return texto

def adicionar_interjeicao(texto, contexto):
    interjeicoes = {
        "pensando": ["hum", "deixe-me ver", "ah, já sei", "interessante", "bom ponto"],
        "empatia": ["entendo", "imagino como você se sente", "com certeza", "eu também já passei por isso", "isso faz sentido"],
        "surpresa": ["uau", "sério?", "não acredito!", "que interessante!", "nossa!"]
    }
    if contexto in interjeicoes:
        interjeicao = random.choice(interjeicoes[contexto])
        return f"{interjeicao}. {texto}"
    return texto