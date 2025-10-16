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
