
# Exercício 1 : 

segundos = int(input("Digite o número de segundos: "))

horas = segundos // 3600

minutos = (segundos % 3600) // 60

seg_finais = segundos % 60

print(f"{horas} hora, {minutos} minuto e {seg_finais} segundos.")


# Exercício 2 :

num1 = (int(input("Digite o 1º número : ")))
num2 = (int(input("Digite o 2º número : ")))
num3 = (int(input("Digite o 3º número : ")))



maior = num2
menor = num1

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

print(f"O maior é o número : {maior}")

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"O menor é o número : {menor}") 