n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

if n1 > n2:
    print(f"O {n1} é o maior valor.")
elif n1 < n2:
    print(f"{n2} é o maior valor")
if n1 == n2:
    print("Não existe maior valor, os dois são iguais")