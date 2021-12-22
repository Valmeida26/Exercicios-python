'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = str(input("Digite m para masculino e f para feminino: "))

if letra == "m":
    print(f"Você é do sexo Masculino {letra}")
elif letra == "f":
    print(f"Você é do sexo Feminino {letra}")
else:
    print("Digite uma letra válida")





