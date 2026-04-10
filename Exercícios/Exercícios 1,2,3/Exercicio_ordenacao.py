nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]
n = len(nomes)
for i in range(n):
    for j in range(0, n - i - 1):
        
        if nomes[j] > nomes[j + 1]:
            
            nomes[j], nomes[j + 1] = nomes[j + 1], nomes[j]