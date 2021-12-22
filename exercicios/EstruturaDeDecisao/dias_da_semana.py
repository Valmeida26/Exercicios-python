'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia= int(input("Digite um número correspondente a um dia da semana: "))
def semana():
    if dia == 1:
        print(f"Você digitou {dia}, esse dia corresponde ao Domingo!!!")
    elif dia == 2:
        print(f"Você digitou {dia}, esse dia corresponde a Segunda!!!")
    elif dia == 3:
        print(f"Você digitou {dia}, esse dia corresponde a Terça!!!")
    elif dia == 4:
        print(f"Você digitou {dia}, esse dia corresponde a Quarta!!!")
    elif dia == 5:
        print(f"Você digitou {dia}, esse dia corresponde a Quinta!!!")
    elif dia == 6:
        print(f"Você digitou {dia}, esse dia corresponde a Sexta!!!")
    elif dia == 7:
        print(f"Você digitou {dia}, esse dia corresponde ao Sábado!!!")
    else:
        print("Digite um número válido!!!")
semana()



