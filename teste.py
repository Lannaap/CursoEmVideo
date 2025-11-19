lista = []
contador = 0

while True:
    nome = input("Digite um nome: ").upper

    if nome == "FIM":
        break

    lista.append(nome)

    if nome[0] == "A":
        contador = contador + 1

print(f"Foram digitados {len(lista)} nomes e {contador} começam com A")