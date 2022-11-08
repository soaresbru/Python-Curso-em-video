print('Vamos jogar Jokenpô')
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
n=int(input('escolha a opção digitando seu número '))
lista=['Pedra','Papel','Tesoura']
from random import randint
m=randint(0,2)
if n==m:
    print('Vocês escolheram o mesmo \n EMPATE')
elif n==0 and m==1 or n==1 and m==2 or n==1 and m==0:
    print(f'''   Você escolheu {lista[n]}
    a Máquina escolheu {lista[m]}
    VOCÊ PERDEU''')
elif n==0 and  m==2 or n==1 and m==0 or n==2 and m==1:
    print(f'''      Você escolheu {lista[n]}
    a Máquina escolheu {lista[m]}
    VOCÊ GANHOU''')
else:
    print('você digitou um número inválido, tente novamente')
