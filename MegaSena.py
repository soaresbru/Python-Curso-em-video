from random import sample
from time import sleep

n=int(input('diga quantas apostas você quer fazer'))
jogos=[]


for i in range(0,n):
    aposta=sorted(sample(range(1,61),6))
    jogos.append(aposta[:])
    print(f'a aposta {i+1} é {aposta} ')
    sleep(1)
