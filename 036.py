vc = float(input("Digite o valar da casa: "))

vs = float(input("Digite o valor da salário: "))

a = float(input("Em quantos anos você quer pagar?: "))

p = a * 12

pr = vc / p

ls = pr * 0.3

if vs < ls:

    print("Emprestimo negado!")

else:
    print("Emprestimo aprovado!")