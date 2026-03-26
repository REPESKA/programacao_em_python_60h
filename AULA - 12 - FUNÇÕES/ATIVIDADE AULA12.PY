print('Exercícios com funções:')

print('Exercícios com funções')

print('variáveis locais, globais e parâmetros')



print('......................................................................')

print('1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS')



numero1 = input ('Digite um Número')
print(numero1)

numero2 = input ('Digite um Número')
print(numero2)

def mostrar_numero():
    numero1  = float(input(numero1))
    numero2 = float (input(numero2))
    print(numero1,numero2)

def mostar_numero():
    print(numero1,numero2)





print('......................................................................')
print(' 2-UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS')


def calculadora():

    n1 = float(input('nº >>'))
    op = input('>>')
    if op == '+': 
       n2 = float(input('>>')) 
       s  = soma(n1,n2)
       print(s)
    elif op == '-': 
       n2 = float(input('>>')) 
       s  = subtracao(n1,n2)
       print(s)
    elif op == '*': 
       n2 = float(input('>>')) 
       s = mult(n1,n2)
       print(s)
    elif op == '/': 
       n2 = float(input('>>')) 
       s = div(n1,n2)
       print('=', s)    




print('......................................................................')

print(' 3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO')


input('Digite um número: ')
lista = [1, 2, 3, 4, 5]
media = numero (lista)
print("Média:", media)











print('......................................................................')


print('4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS')


numero  = input('Digite seu ano de nascimento: ')
numero2 = 2026

def soma():
    somando = int(numero) - numero2
    print(somando)

soma()    

elif int(numero) ==>18:
    print('Parabéns, você tem 18 anos!')







print('......................................................................')
print(' 5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA')


numero  = input('Digite seu ano de nascimento: ')
numero2 = 2026

def soma():
    somando = int(numero) - numero2
    print(somando)

soma()    




print('......................................................................')
print('6 - DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999')


numero  = input('Digite um Ano: ')
lista = [1958,1962,1970,1994,2002]

def soma():
    somando = int(numero) - numero2
    print(somando)

soma()    

elif int(numero) in lista:
    print('Parabéns, você acertou em cheio')

        








print('......................................................................')
print('7 - DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.')

print ('1 -Função -  cumprimentar o cliente, 2 - Função - restaurante, 3 - Sugestão utilize listas  e loops')


def cumprimento(nome):
    return 'olá', nome

def produto(lista_prod, prod, carrinho, meus_v, lista_valores, paga):

    carrinho.append(lista_prod[prod])
    meus_v.append(lista_valores[paga])
    return carrinho,'R$',  float(sum(meus_v))


def pagamento(lista_tip_pags, escolha_pag):
    return lista_tip_pags[escolha_pag]




def restaurante():
   
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    valores  = [0,100,60,150,250]
    carrinho = []
    meus_valores = []
    nome = input('Nome: ')
    print(cumprimento(nome))
 
    for p, v in enumerate(zip(menu, valores)):
        print(p,'R$', v)    

    acrescentar =  input('deseja acrescentar ao carrinho? ')
    while acrescentar == 'sim':    
        e  =  int(input('Escolha seu produto: 1 ,2 ,3, 4'))
        print( produto(menu, e, carrinho, meus_valores,valores, e ))
        acrescentar = input('Deseja continuar? ')
 
    else:
        lista_pag = ['', '1 pix', '2 CC', ' 3 CD']
        escolha =  int(input(f'Escolha a forma de pagamento,  {lista_pag}'))
        print(pagamento(lista_pag, escolha))
        print('Obrigado volte SEMPRE!')    




restaurante()