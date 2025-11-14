n = str(input('Digite seu nome: ')).strip().split()
print(f"Seu primeiro nome é: {n[0].upper()}")
print(f"Seu segundo nome é: {n[len(n)-1].upper()}")