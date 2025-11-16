n1 = float(input("Digite a primeira nota: "))

n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2)/2

if m < 5.0:
    print("Reprovado")

if m >= 5.0 or m <= 6.9:
    print("Em Recuperação")
if m >= 7.0:
    print("Aprovado")
