
import random

banco_perguntas = [

'',
'1 - O que é, o que é? Tem pernas, mas não anda; tem braços, mas não abraça.?',
'2- O que é, o que é? Nasce branco, fica verde, depois fica vermelho e acaba preto.?',
'4 - O que é, o que é? Cai em pé e corre deitada?',
'5 - O que é, o que é? Tem coroa, mas não é rei; tem escamas, mas não é peixe?',
'6 - O que é, o que é? Quanto mais se tira, mais se tem?',
'7 - O que é, o que é? Tem pescoço e não tem cabeça, tem braços e não tem mãos?',
'8 - O que é, o que é? Passa diante do sol e não faz sombra?',
'9 - O que é, o que é? Quebra-se se não for segurado com as duas mãos?',
'10 - O que é, o que é? Tem cidade, mas não tem casas; tem rio, mas não tem água?',
'O que é, o que é? Anda com os pés na cabeça?',


]
respostas = [
'',

'1 - A cadeira',
'2- O café',
'3- A chuva',
'4 - O abacaxi',
'5 - O buraco',
'6 - A camisa',
'7 - O vento',
'8 - A promessa',
'9 - O mapa',
'10 - O piolho',

]

print('JOGO DE PERGUNTAS ACERTE E GANHE 1 MILHÃO')
print('***' * 20)
maquina  =  random.choice(banco_perguntas)
id_maquina =  banco_perguntas.index(maquina)
print(maquina)
print('***' * 20)

print('ESCOLHA SUA RESPOSTA')
r = int(input(f'''
{respostas[1]} , {respostas[2]} , {respostas[3]}
{respostas[4]} , {respostas[5]} , {respostas[6]}
{respostas[7]} , {respostas[8]} , {respostas[9]}
{respostas[10]} ,     
'''))

if r == id_maquina:
    print('acertou em cheio')
    print('A sua resposta é', respostas[r])
    print('A resposta corrtw é ', respostas[id_maquina] )
else:
    print('Errou feio')
    print('A sua resposta é', respostas[r])
    print('A resposta corrtw é ', respostas[id_maquina] )


# else ou elif

print(r)
print(id_maquina)