p = float(input("Digite o preço: "))

Fp = int(input("Digite a forma de pagamento: "))

print("Pagamento à vista (dinheiro/pix): [1]\n À vista no cartão:[2]\n Em até 2x no cartão:[3]\n 3x ou mais no cartão:[4]")

if Fp == 1:
    print(f"O valor do produto com 10% de desconto ficou por {p-(p*10/100)}")
    if Fp == 2:
        print(f"O valor do produto com 5% de desconto ficou por {p-(p*5/100)}")
    if Fp == 3:
        print(f"O valor do produto com 20% de juros ficou por {p+(p*20/100)}")