'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
lista = []
quantidade = 3
for i in range (quantidade):
    numero = int(input("Digite um número: "))
    lista.append(numero)

lista.sort(reverse = True) #faz a ordem decrescente
print(lista)

