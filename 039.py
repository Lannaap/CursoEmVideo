from datetime import date

y = date.today().year

a = int(input("Digite o ano de nascimento: "))

i = y - a

if i < 18:
    print(f"Ainda irá se alistar pois faltam {18-i} anos")

if i == 18:
    print("Está na hora de se alistar")

if i > 18:
    print(f"Já passou da hora de se alistar pois passou {i-18} anos")