preço1  = input ( "Digite o preço do produto 1: " )
preço1  = float(preço1)
preço2  = input ( "Digite o preço do produto 2: " )
preço2  = float(preço2 )
preço3  = input ( "Digite o preço do produto 3: " )
preço3  = float(preço3)
maior = preço1
if preço2 > preço1 and preço2 > preço3:
    maior = preço2
if preço3 > preço1 and preço3 > preço2:
    maior = preço3
menor = preço1
if preço2 < preço3 and preço2 < preço1:
    menor = preço2
if preço3 < preço2 and preço3< preço1:
    menor = preço3
print(f"O menor preço foi {menor}")
print(f"O maior preço foi {maior}")
