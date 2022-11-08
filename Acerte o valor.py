print('Sou seu computador...')
print('Acabei de pensar em número de 0 a 10')
print('Será que você consegue adivinhar qual foi')

from random import randint
n=randint(0,10)
t=11
q=0
while t!=n:
    t=int(input('Qual é o seu palpite? '))
    if t>n:
        print('Menos ... tente outro palpite ')
    else:
        print('Mais ... tente outro palpite ')
    q+=1
print(f'Você acertou com {q} tentativas')
print('PARABÉNS !!!!!!!!!!!!')
