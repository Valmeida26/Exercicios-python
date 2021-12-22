'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos).'''

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade de download em MBPS: "))

tempo = tamanho_arquivo/velocidade

print(f"O seu arquivo tem {tamanho_arquivo} MB e esta sendo baixado em um "
      f"link de {velocidade} MBS, o download será comcluido em {tempo:.2f} segundos.")