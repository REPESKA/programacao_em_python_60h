# import random

# for chances in range(3,0,-1):
#     a  =  random.randint(1,60)
#     print('você tem, ', chances, 'chances')
#     chute  = int(input('Digite seu chute: '))
   
#     if a  ==  chute:
#         print('Ganhou!! acertou em cheio!')
#         break  
#     else:
#         print('errou feio... ')
#         # if chances == 0:

       

nomes = []
idades = []
cidades = []

for cad in range(10):
    nome =  input('Nome: ')
    idade = input('Idade: ')
    cidade  =  input('Cidade: ')
    nomes.append(nome)
    idades.append(idade)
    cidades.append(cidade)