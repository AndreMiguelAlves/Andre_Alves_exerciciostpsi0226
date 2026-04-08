num = 2   
primos= 0

while primos< 10:
    divisores = 0
    for i in range(2, num):
        if num % i == 0:
            divisores += 1
            break
    if divisores == 0:
        print(num)
        primos+= 1
    num += 1