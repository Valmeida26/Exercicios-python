'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo
 o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input("Digite o seu salário: "))
aumento1 = salario*0.20
aumento2 = salario*0.15
aumento3 = salario*0.10
aumento4 = salario*0.05
salario_final1 = salario + aumento1
salario_final2 = salario + aumento2
salario_final3 = salario + aumento3
salario_final4 = salario + aumento4
def reajuste():
    if salario <= 280.0:
        print(f"O seu salário era {salario} agora você terá um aumento de 20% ficando em {salario_final1}, seu aumento foi de {aumento1}")
    elif salario > 280.0 and salario <= 700.0:
        print(f"O seu salário era {salario} agora você terá um aumento de 15% ficando em {salario_final2}, seu aumento foi de {aumento2}")
    elif salario > 700.0 and salario <= 1500.0:
        print(f"O seu salário era {salario} agora você terá um aumento um aumento de 10% ficando em {salario_final3}, seu aumento foi de {aumento3}")
    elif salario > 1500.0:
        print(f"O seu salário era {salario} agora você terá um aumento um aumento de 5% ficando em {salario_final4}, seu aumento foi de {aumento4}")
reajuste()








