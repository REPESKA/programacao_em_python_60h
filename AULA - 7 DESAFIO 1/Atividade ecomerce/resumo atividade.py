ecommerce = {

'prod1 ':'Carros',
'prod2':'Motos',
'prod3': 'Drones'

}

ecommerce = {


'carros':{
    print['mercedes','Bugati','Pagani'],[input('Digite o modelo do carro:').lower(input('Digite a marca do carro:').lower())],

    Mercedes = ['Classe A', 'Classe C', 'Classe E'], classes = ['A', 'C', 'E'],
    Bugati = ['Chiron', 'Divo', 'Centodieci'],
    Pagani = ['Zonda', 'Huayra', 'Imola'],

    },



'Motos':{['Kawasaki', 'Ducati','Harley daivson'],input('Digite o modelo da moto:').lower(input('Digite a marca da moto:').lower())],}


'Drones': {['4F', 'Matrice', 'Avata2']input('Digite o modelo do drone:').lower(input('Digite a marca do drone:').lower())],}

}

print(ecommerce['carros'][input('Digite a marca do carro:').lower()][input('Digite o modelo do carro:').lower()]) 

print(ecommerce['Motos'][input('Digite a marca da moto:').lower()][input('Digite o modelo da moto:').lower()])

print(ecommerce['Drones'][input('Digite a marca do drone:').lower()][input('Digite o modelo do drone:').lower()])


carrinho = input('Digite o produto que deseja comprar:').lower()
if carrinho in ecommerce['carros']:
    print('Produto adicionado ao carrinho')
elif carrinho in ecommerce['Motos']:
    print('Produto adicionado ao carrinho') 
elif carrinho in ecommerce['Drones']:
    print('Produto adicionado ao carrinho')

