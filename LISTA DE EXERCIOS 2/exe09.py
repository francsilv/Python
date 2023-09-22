valor_h = int(input('valor da hora: '))
total_h = int(input('total  hora: '))
salario = valor_h * total_h

if (salario <= 900):
    percentual = 0
elif (salario <= 1500):
    percentual = 5
elif (salario <= 2500):
    percentual = 10
else:
    percentual = 20

print('valor_h: R$ ', valor_h)
print('total_h: R$ ', total_h)
print('Percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)