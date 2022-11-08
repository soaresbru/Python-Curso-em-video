tot={}
part=[]
jogador=[]
while True:
    tot['nome']=str(input('Digite o nome do jogador '))
    m=int(input(f'Quantas partidas o {tot["nome"]} jogou '))
    for i in range(0,m):
        part.append(int(input(f'Quantos gols o jogador fez na partida {i+1} : ')))

    tot['gols']=part[:]
    tot['total']=sum(part)
    part.clear()
    jogador.append(tot.copy())
    tot.clear()
    k=str(input('Deseja adionar mais um jogador (S/N)? ')).strip().lower()
    if k in 'n':
        break

print(jogador)
print('#####################################')
print(f'cod  {"nome":<20}  {"gols":<15}  {"total":<6}')
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
for i, v in enumerate(jogador):
    print(f'{i}    {v["nome"]:<20}  {str(v["gols"]):<15}  {v["total"]:<6} ')

while True:
    j=int(input("Qual jogador você deseja (999 para parar)"))
    if j==999:
        break
    elif j<0 or j>len(jogador):
        print('Jogador inválido')
    else:
        for i, v in enumerate(jogador):
            if i==j:
                print(f'levantamento do {v["nome"]}')
                for l in range(0,len(v['gols'])):
                    print(f'no jogo {l+1} fez {v["gols"][l]}')