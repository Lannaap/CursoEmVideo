v = int(input("Digite a velocidade do carro: "))
l = 80
m = v - l
if v <= l:
    print("Você não ultrapassou o limite.")
else:
    print(f"Você ultrapassou {v-l:.2f} km a mais do limite e deve R${m*7:.2f} de multa")
