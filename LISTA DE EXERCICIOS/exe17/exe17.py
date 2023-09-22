import math
metragem = input("Qual o valor de metros quadrados que você deseja pintar? ")
metragem = float(metragem)

litros = metragem / 6

latas_fechadas = math.ceil(litros / 18)
valor_latas = round(latas_fechadas * 80,2)
valor_latas = str(valor_latas)
latas_fechadas = str(latas_fechadas)
print("Você de precisa de " + latas_fechadas + " latas fechadas.")
print("O total das latas fechadas é: R$"+valor_latas)

galoes_fechados = math.ceil(litros / 3.6)
valor_galoes = round(galoes_fechados * 25,2)
valor_galoes = str(valor_galoes)
galoes_fechados = str(galoes_fechados)
print("Você de precisa de " + galoes_fechados + " galões fechados.")
print("O total dos galões fechados é: R$"+valor_galoes)

latas_com_sobra = math.floor(litros / 18)
valor_latas_sobra = round(latas_com_sobra * 80,2)

sobra_litros = litros - (latas_com_sobra * 18)
latas_com_sobra = str(latas_com_sobra)

galoes_apos_sobra = math.ceil(sobra_litros / 3.6)
valor_galoes_sobra = round(galoes_apos_sobra * 25,2)
galoes_apos_sobra = str(galoes_apos_sobra)

valor_lata_galao = valor_latas_sobra + valor_galoes_sobra

valor_latas_sobra = str(valor_latas_sobra)
valor_galoes_sobra = str(valor_galoes_sobra)
valor_lata_galao = str(valor_lata_galao)
print("Você de precisa de " + latas_com_sobra + " latas e "+ galoes_apos_sobra +" galões.")
print("O total das latas e dos galões é: R$"+valor_lata_galao)