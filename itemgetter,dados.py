tot={}
n=[]
from random import randint
from operator import itemgetter
for i in range(1,5):
    tot[f'jogador {i}']=randint(1,6)

n=(sorted(tot.items(), key=itemgetter(1), reverse=True))

for k in n:
    print(f'{k[0]} tirou no dado {k[1]}')
