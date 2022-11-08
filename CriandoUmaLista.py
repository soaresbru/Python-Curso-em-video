lista=[]
for i in range (1,6):
    n=float(input(f'Qual é o peso da pessoa {i} é Kg: '))
    lista+=[n]
print(f'o peso maximo foi KG {max(lista)}')
print(f'O peso minimo foi Kg {min(lista)}')

