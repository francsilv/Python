altura = input("Digite a sua altura: ")
altura = float(altura)

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_h = str(peso_ideal_h)
peso_ideal_m = (62.1 * altura) - 44.7
peso_ideal_m = str(peso_ideal_m)

print("Peso ideal para homens: "+peso_ideal_h)
print("Peso ideal para mulheres: "+peso_ideal_m)