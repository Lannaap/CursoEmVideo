a = float(input("Digite sual altura: "))

p = float(input("Digite o peso: "))

imc = p / (a*a)

print(f"seu imc é de {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso!")

if imc >= 18.5 and imc <= 25:
    print("Peso ideal!")

if imc >= 25 and imc <= 30:
    print("Sobrepeso!")

if imc >= 30 and imc <= 40:
    print("Obesidade!")

if imc == 40:
    print("obesidade morbida")