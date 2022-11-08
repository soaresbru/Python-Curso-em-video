boletim=list()
aluno=list()

while True:
    aluno.append(str(input('Qual é o nome do aluno? ')))
    aluno.append(float(input('Quanto ele tirou na primeira prova ')))
    aluno.append(float(input('Quanto ele tirou na segunda prova ')))
    boletim.append(aluno[:])
    aluno.clear()
    n=str(input('Deseja adicionar mais um aluno? (S/N)')).strip().lower()
    if n=='n':
        break
print('********* BOLETIM ********')
for i in range(0,len(boletim)):
    print(f'{i+1:<}    {boletim[i][0]:^20}   media: {(boletim[i][1]+boletim[i][2])/2 :.2f}')
print('#################################')
while True:
    m=int(input('Qual aluno você quer ver a nota? digite o número do aluno (digitar 999 encerra o programa) '))
    if m==999:
        break
    for i in range(0,len(boletim)):
        if i+1==m:
            print(f'na prova 1 tirou {boletim[i][1]} e na prova 2 tirou {boletim[i][2]}')
print('¨¨¨¨¨¨¨¨¨¨¨¨¨FIM¨¨¨¨¨¨¨¨¨¨¨¨')
