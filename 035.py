r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 :
    print("Forma triangulo")
else:
    print("Não forma triangulo")