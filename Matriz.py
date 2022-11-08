
total=[[0,0,0],[0,0,0],[0,0,0]]
totpar=totcol=maior=0
for i in range(0,3):
    for j in range(0,3):
        total[i][j]=(int(input(f'digite o valor da matrix ({i},{j})')))
        if total[i][j] %2==0:
            totpar+=total[i][j]
        if total[i][2]:
            totcol+=total[i][2]
        if total[1][0]:
            maior=total[1][0]
        elif total[1][j]>maior:
            maior=total[1][j]
for i in range(0,3):
    for j in range(0,3):
        print(f'[{total[i][j]:^4}]', end=' ')
    print()
print('***********************************************')
print(f'a soma dos pares é {totpar}')
print(f'a soma da coluna 3 é {totcol}')
print(f'o maior valor da linha 2 é {maior}')
