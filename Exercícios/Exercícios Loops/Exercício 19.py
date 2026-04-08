num = 60  


a, b = 1, 1

print("Série : ")
print(a, b, end=" ")  


for i in range(num - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c 