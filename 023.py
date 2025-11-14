 #Fazer um programa que leia um número de 0 ao 9999 e mostre na tela cada um dos digitos separados. Ex: Digite um número: 1834
# unidade: 4 , dezena: 3 , centena: 8 , milhar: 1
n = int(input("Digite um numero: "))
print(f"A unidade é: {n // 1 % 10 }, a dezena é: {n // 10 % 10}, a centena é: {n // 100 % 10}, e milhar: {n // 1000 % 10}")
