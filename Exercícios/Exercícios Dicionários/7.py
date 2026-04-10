d = {'a': 1, 'b': 2, 'c': 3}
novo_d = {}


for chave, valor in d.items():
    novo_d[valor] = chave

print(novo_d)
