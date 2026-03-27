
import os

# Criar um arquivo  "with"
with open('novo_diretorio', 'w') as novo_arquivo:
    os.mkdir('novo_arquivo')
    


with open('exemplo.txt', 'r') as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)