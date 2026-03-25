print('Exercício 1:')
print ('Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.')


a = int(input())
b = int(input())

try:
      print(a/b)

except ZeroDivisionError as error:
      print(error)

else:
      print( ' Sem erros')

finally:
      print('Aqui sempre vai printar')

print('....................................................................................................')


print('Exercício 2:')
print('Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.')



def divisao():

    try:
      a = float(input('>>'))
      b = float(input('>>'))
      div = a/b
      print(div)  
    except ZeroDivisionError:
        print("A divisão não ser por zero")
    except ValueError:
        print('Um texo foi digitado')
    except TypeError as erro:
        print(erro)

    else:
        print('Algo deu errado ')    



divisao()

print('..........................................................................................')



print('Exercício 3:')
print('Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).')

try:   
    l = [123,5,3]
    print(l[2] / 0)
except NameError:
    print('declare a variavel do dado')    
except TypeError:
    print('Dados no calculo aritmetico incorreto')    
except ValueError:
    print('Valor inserido incorretamente')
except ZeroDivisionError:
    print('A divisão não pode ser por zero')
except IndexError:
    print('Esse indice nãi existe')
else:
    print('Erro desconhecido')
finally:
    print('FIM de carregamento')