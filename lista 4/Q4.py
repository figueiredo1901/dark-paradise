import random

def embaralha_palavra(palavra):
    palavra = palavra.lower()
    lista_letras = list(palavra)
    random.shuffle(lista_letras)
    return ''.join(lista_letras)

palavra = input("Digite uma palavra: ")
print(f"Palavra embaralhada: {embaralha_palavra(palavra)}")
