import random
n1 =str(input('Digite o nome do primeiro aluno: '))
n2 =str(input('Digite o nome do segundo aluno: '))
n3 =str(input('Digite o nome do tereiro aluno: '))
n4 =str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
ordem = random.sample(lista, k=4)
print(f"A ordem de apresentacao será: {ordem}")
