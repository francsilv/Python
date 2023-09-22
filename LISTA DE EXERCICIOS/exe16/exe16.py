import math
metragem = input("Qual o valor de metros quadrados que você deseja pintar? ")
metragem = float(metragem)

litros = metragem / 3
latas = litros / 18
latas = math.ceil(latas)
valor = latas * 80
valor = round(valor,2)

latas = str(latas)
valor = str(valor)

print("Você precisa de "+latas+" latas de tintas")
print("O valor total é: R$"+valor)