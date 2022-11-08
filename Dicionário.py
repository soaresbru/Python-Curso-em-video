total=[]
pessoa={}
cont=soma=0
while True:
    pessoa['nome']=str(input('Qual é o nome da pessoa '))
    while True:
         pessoa['sexo']=str(input('Qual é o sexo (M/F):  ')).strip().upper()
         if pessoa['sexo'] in 'MF' :
             break
         print('erro de digitação tente novamente')
    pessoa['idade']=int(input('Qual é a idade: '))
    total.append(pessoa.copy())
    cont+=1
    while True:
        n=str(input('Deseja adicionar mais uma pessoa (S/N)? ')).strip().lower()
        if n in 'sn':
            break
        else:
            print('Ocorreu um erro tente novamente')
    if n=='n':
            break
    print('#################################')
print(f'Foram cadastradas {cont} pessoas')
for i in total:
    soma+=(i['idade'])
print(f'A média de idade é {soma/cont} ')
print('o nome das mulheres é ', end='')
for i in total:
    if i['sexo']=='F':
        print(i['nome'],)
print('As idades acima da média são: ', end='')
for i in total:
    if i['idade']>(soma/cont):
        print(f'{i["idade"]}  ')
