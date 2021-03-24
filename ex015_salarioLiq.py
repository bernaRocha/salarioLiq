#Código em python para cálculo de salário líquido.

salarioHora = int(input("Quanto você ganha por hora? "))
horaMes = int(input("Quantas horas você trabalha durante o mês? "))

salarioBruto = salarioHora * horaMes
print("Salário bruto: $ {}".format(salarioBruto))

ir = (salarioBruto * 11)/100
print("IR (11%): {}".format(ir))

inss = (salarioBruto * 8)/100
print("INSS (8%): {}".format(inss))

sindicato = (salarioBruto * 5)/100
print("Sindicato (5%): {}".format(sindicato))

salarioLiquido = salarioBruto - ir - inss - sindicato
print("Seu salário liquido é {}: $".format(salarioLiquido))