# 1. Pedir a frase ao utilizador
frase = input("Introduz uma frase: ")

palavras = frase.split()

contagem = {}

for p in palavras:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1

print(contagem)