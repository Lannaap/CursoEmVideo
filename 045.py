import random

# 1 = pedra
# 2 = papel
# 3 = tesoura

r = random.randint(1, 3)

eu = input("Escolha entre pedra, papel ou tesoura: ").lower()

if eu == "pedra":
    eu_n = 1
elif eu == "papel":
    eu_n = 2
elif eu == "tesoura":
    eu_n = 3
else:
    print("Opção inválida!")
    exit()

print(f"Você escolheu {eu}")
print(f"O computador escolheu {r}")


if eu_n == r:
    print("Empate!")


elif (eu_n == 1 and r == 3) or (eu_n == 2 and r == 1) or (eu_n == 3 and r == 2):
    print("Você venceu!")

else:
    print("Você perdeu!")
