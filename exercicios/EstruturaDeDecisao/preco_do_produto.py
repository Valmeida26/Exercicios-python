'''Faça um programa que pergunte o preço de três produtos e informe qual produto
 você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))

def menor_preco():
    if p1 < p2 and p3:
        print(f"O produto P1 R${p1} deve ser escolhido pois ele tem o menor preço.")
    if p2 < p1 and p3:
        print(f"O produto P2 R${p2} deve ser escolhido pois ele tem o menor preço.")
    if p3 < p1 and p2:
        print(f"O produto P3 R${p3} deve ser escolhido pois ele tem o menor preço.")
    #caso sejam iguais os valores
    if p1 == p2 and p1 and p2 < p3:
        print(f"Os produtos P1 e P2 R${p1}, R${p2} devem ser escolhidos pois eles tem o menor preço.")
    if p1 == p3 and p1 and p3 < p2:
        print(f"Os produtos P1 e P3 R${p1}, R${p3} devem ser escolhidos pois eles tem o menor preço.")
    if p2 == p3 and p2 and p3 < p1:
        print(f"Os produtos P2 e P3 R${p2}, R${p3} devem ser escolhidos pois eles tem o menor preço.")
    elif p1 == p2 and p3:
        print("Os três produtos tem preços iguais")
menor_preco()