print() 
print() 

print('SISTEMA DE VERIFICAÇÃO DE MÉDIA')
print() 
nome = input('Digite o nome do aluno: ')
print() 
print('Olá,', nome, 'vamos calcular a média das suas notas.')
print() 

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

print() 
print ('***' * 15)

print('A média das notas de', nome, 'é:', media)
print() 

if media >= 7:

    print('Aprovado')
    print('Continue assim!')


elif media >= 5:

    print('Recuperação')
    print('Estude mais para melhorar sua nota.')
 
elif media <= 4:
    print ('Reprovado')
    print ('É importante dedicar mais tempo aos estudos.')
    

    
