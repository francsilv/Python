valor_hora = input("Digite quanto você ganha por hora: ")
valor_hora = float(valor_hora)
horas = input("Digite quantas horas você trabalhou: ")
horas = int(horas)

salario_bruto = valor_hora * horas
salario_bruto = round(salario_bruto,2)
ir = salario_bruto * 0.113
ir = round(ir,2)
inss = salario_bruto * 0.08
inss = round(inss,2)
sindicato = salario_bruto * 0.05
sindicato = round(sindicato,2)

salario_liquido = salario_bruto - ir - inss - sindicato

salario_bruto = str(salario_bruto)
ir = str(ir)
inss = str(inss)
sindicato = str(sindicato)
salario_liquido = str(salario_liquido)

print("+ Salário Bruto : R$"+salario_bruto)
print("- IR (11%) : R$"+ir)
print("- INSS (8%) : R$"+inss)
print("- Sindicato (5%) : R$"+sindicato)
print("= Salário Liquido : R$"+salario_liquido)