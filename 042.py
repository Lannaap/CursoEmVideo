r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Forma um triangulo")

    if r1 == r2 == r3:
        print("Tipo: Equilátero (todos os lados iguais)")

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("Tipo: Isósceles (dois lados iguais)")

    else:
        print("Tipo: Escaleno (todos os lados diferentes)")

else:
    print("Não forma um triangulo")