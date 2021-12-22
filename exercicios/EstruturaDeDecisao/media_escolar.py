'''Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez'''

n1 = float(input("Digite a nota de matemática: "))
n2 = float(input("Digite a nota de português: "))
media = (n1 + n2) / 2

if media >= 7:
    print(f"Sua nota foi {media}, parabens você foi APROVADO")
elif media <= 7:
    print(f"Sua nota foi {media}, infelizmente você foi REPROVADO")
if media == 10:
    print(f"Sua nota foi {media}, parabens você foi APROVADO COM LOUVOR")