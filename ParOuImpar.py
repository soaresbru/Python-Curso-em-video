print('Jogo Par ou Impar')
from random import randint
soma=0
while True:
    print('*************************************************')
    m=str(input('Você quer Par(digite p) ou Ímpar(digite i)')).strip().lower()
    if m!= 'p' and m!='i':
        m = str(input('Você quer Par(digite p) ou Ímpar(digite i)')).strip().lower()
    n=int(input('digite um número'))
    c=randint(0,10)
    if m=='p' and (n+c)%2 ==0 :
        print(f'você escolheu {n} e a máquina {c}, deu PAR')
        print(f'PARABÉNS !!!!!!!!!!!')
        soma+=1
    elif m=='i' and (n+c)%2 !=0:
        print(f'Você escolheu {n} e a máquina {c}, deu IMPAR')
        print(f'PARABÉNS !!!!!!!!!!!!')
    else:
        print('*****************************************')
        print(f'você escolheu {n} e a máquina {c}')
        print('Você Perdeu')
        print(f'Você ganhou {soma} partidas')
        break
