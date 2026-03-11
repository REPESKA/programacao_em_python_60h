banco_dados =  {}

print('Olá, Seja Muito Bem-vindo - HOTEL GUARULHOS')

nome1 = input('Nome,😁')
idade1 = input('Idade')
senha1 = input('Senha')

nome2 = input('Nome,😁')
idade2 = input('Idade')
senha2 = input('Senha')

nome3 = input('Nome,😁')
idade3 = input('Idade')
senha3 = input('Senha')

banco_dados['nomes'] = [nome1, nome2, nome3]
banco_dados['idades'] = [idade1, idade2, idade3]
banco_dados['senhas'] = [senha1, senha2, senha3]

(banco_dados)


 

login_nome = input('Digite seu nome >>')
senha_acesso = input('Digite sua senha >> ')


if login_nome in banco_dados['nomes'] and senha_acesso in banco_dados['senhas']:
    print('Seja bem vindo ao sistema!')
    
    print('Escolha o quarto: ', banco_dados['nomes'][0])
    quartos  = ['','simples🛏️', 'duplo🛏️🛏️', 'luxo🛌🔝']
    valores  =  ['',100,150,250]
    print('quartos:  ', quartos)
    escolha  =  int(input(' 1  Simples🛏️ |  2 Duplo🛏️🛏️ |  3  Luxo🛌🔝')) 
    qd  =  int(input('Quantidade de dias '))
    calculo = qd * valores[escolha]
    print('Vocês escolheu o quarto', quartos[escolha], 'Quant. Dias', qd)
    print('Total a pagar R$', round(calculo,2))
    
    print('Escolha o quarto: ', banco_dados['nomes'][1])
    quartos  = ['','Simples🛏️', 'Duplo🛏️🛏️', 'Luxo🛌🔝']
    valores  =  ['',100,150,250]
    print('quartos:  ', quartos)
    escolha  =  int(input(' 1  Simples🛏️ |  2 Duplo🛏️🛏️ |  3  Luxo🛌🔝')) 
    qd  =  int(input('Quantidade de dias '))
    calculo = qd * valores[escolha]
    print('Vocês escolheu o quarto', quartos[escolha], 'Quant. Dias', qd)
    print('Total a pagar R$', round(calculo,2))    
    
    print('Escolha o quarto: ', banco_dados['nomes'][2])
    quartos  = ['','simples', 'duplo', 'luxo']
    valores  =  ['',100,150,250]
    print('quartos:  ', quartos)
    escolha  =  int(input(' 1  Simples🛏️ |  2 Duplo🛏️🛏️ |  3  Luxo🛌🔝')) 
    qd  =  int(input('Quantidade de dias '))
    calculo = qd * valores[escolha]
    print('Vocês escolheu o quarto', quartos[escolha], 'Quant. Dias', qd)
    print('Total a pagar R$', round(calculo,2))
    
else:
    print('Acesso negado, tente novamente!') 