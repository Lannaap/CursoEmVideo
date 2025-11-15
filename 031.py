d = int(input("Digite a distancia da viagem: "))
if d <= 200:
    print(f"O preço da passagem será de R${d*0.50:.2f}")
else:
    print(f"O preço da passagem será de R${d*0.45:.2f}")