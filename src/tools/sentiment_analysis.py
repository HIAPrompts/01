from textblob import TextBlob

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    if blob.sentiment.polarity > 0.1:
        return "positivo"
    elif blob.sentiment.polarity < -0.1:
        return "negativo"
    else:
        return "neutro"
