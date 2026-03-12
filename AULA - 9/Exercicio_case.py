print('EXERCÍCIOS com match/ case:')



print ('1 - Verificando se o número é par ou ímpar')


numero = int(input('numero; '))

match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('impar')    




print('.......................................................................................................................')
print('2 -  Verificando se um número é positivo, negativo ou zero')


numero = int(input('numero; '))
match numero: 
    case numero if numero > 0:
        print('Positivo')
    case numero if numero < 0:
        print('Negativo')
    case _:
        print('Zero')    





print('.......................................................................................................................')
print('3 -  Verificando se uma string é vazia ou não')


string = input('texto = ')

match string:
   case '':
       print('Vazia')
   case _:
       print('Cheia')





print('.......................................................................................................................')
print('4 -  Verificando se um número é maior, menor ou igual a 10')



numero = int(input('numero; '))
match numero:
    case x if numero > 10:
        print('maior que 10')
    case x if numero < 10:
        print('Menor que 10') 
    case _:
        print('10') 




print('.......................................................................................................................')
print('5 - Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35/64, idoso(65)')
 


idade  =  int(input('idade: '))

match idade:
    
    case x if x >1 and x < 12:
        print('Crianca')
    case x if x >=13 and x <=17:
        print('Adolescente') 
    case x if x >=18 and x <=35:
        print('jovem')
    case x if x >= 35 and x <64:
        print('Adulto')
    case _:
        print('Idoso')         



print('.......................................................................................................................')