import random
n1 = int(input("Digite um numero: "))
n = random.randint(1, 10)
if n1 == n:
    print("Você acertou")
else:
    print("Você errou")
    print(n)