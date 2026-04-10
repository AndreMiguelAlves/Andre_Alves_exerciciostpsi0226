total = 0       
contador = 0    

while contador < 30:
    num = int(input(f"Digite o {contador + 1}º número par (entre 1 e 50): "))
    
   
    if num < 1 or num > 50:
        print("Número inválido! Deve estar entre 1 e 50.")
        continue
    if num % 2 != 0:
        print("Número inválido! Deve ser par.")
        continue
    
    
    total += num
    contador += 1


media = total / 30

print(f"A média dos 30 números pares digitados é: {media}")
