n = int(input('Digite um número inteiro: '))

print("Escolha uma base de conversão: \n [1] converter para Binário \n [2] converter para Octal \n [3] converter para Hexadecimal")

o = int(input('Escolha a opção: '))

if o == 1:
    print(f"{n} convertido para Binário é igual a: {bin(n)[2:]}")

    if o == 2:
        print(f"{n} convertido para Octal é igual a: {oct(n)[2:]}")

    elif o == 3:
        print(f"{n} convertido para Hexadecimal é igual a: {hex(n)[2:]}")
else:
    print("Você não escolheu uma das opções.")