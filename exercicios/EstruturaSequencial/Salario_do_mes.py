'''Faça um Programa que pergunte quanto você ganha por hora e o número de
 horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
 sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido'''

ganha_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalhou: "))

salario = ganha_hora * horas_trabalhadas
imposto_de_renda = salario * 0.11
INSS = salario * 0.08
sindicato = salario * 0.05
salario_final = salario - imposto_de_renda - INSS - sindicato

print(f"Você trabalhou {horas_trabalhadas}, e o total a receber de salário será R${salario} sem descontos.")
print(f"Você pagou de imposto de renda R${imposto_de_renda} reais, ao INSS R${INSS} reais e ao sindicato R${sindicato} reais")
print(f"Você trabalhou bem esse mês e seu salario bruto será R${salario_final:.2f}")





