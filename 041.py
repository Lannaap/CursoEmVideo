from datetime import datetime
y = datetime.now().year

while True:

    ano = int(input("Digite o ano de nascimento: "))

    i = y - ano

    if i <= 9:
        print("Categoria: Mirim")

    if i <= 14:
        print("Categoria: Infantil")

    if i <= 19:
        print("Categoria: Junior")

    if i <= 20:
        print("Categoria: Senior")

    if i > 20:
        print("Categoria: Master")

    c = str(input("Deseja preencher novamente?(S/N): ")).upper()

    if c == "N":
        print("Encerrando...")
        break
#BUG ACONTECENDO QUANDO TEM 2 IDADES NO MESMO ANO. NO CASO PARA SER MAIS PRECISO É NECESSARIO COLOCAR MES DE NASCIMENTO