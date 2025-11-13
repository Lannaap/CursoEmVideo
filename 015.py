Di = float(input("Quantos Dias? "))
km = float(input("Quantoas Km? "))
d = Di * 60
k = km * 0.015
print(f"O preço do aluguel a ser pago é de R${d+k:.2f}")