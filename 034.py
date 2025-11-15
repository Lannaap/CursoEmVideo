s = float(input("Digite o seu salario: "))
if s >= 1250.00:
    print(f"Seu salario teve um aumento de 10% e ficou R${s+(s*10/100):.2f}")
else:
    print(f"Seu salario teve um aumento de 15% e ficou R${s+(s*15/100):.2f}")