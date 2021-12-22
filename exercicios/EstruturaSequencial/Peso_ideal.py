'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = str(input("Seu sexo é masculino ou feminino? digite m para masculino e f para feminino: \n "))
altura = float(input("Digite a sua altura: "))

homem = (72.7*altura) - 58
mulher = (62.1*altura) - 44.7

if sexo == "m":
    print(f"O seu peso ideal é: {homem}")
elif sexo == "f":
    print(f"O seu peso ideal é: {mulher}")


