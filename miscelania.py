from random import choice
print("====VAMOS DESCOBRIR QUEM É O MELHOR PRIMO(A) DO BRUNO?==")
n1=input("Digite o nome de um primo ")
n2=input("Digite o nome de mais um primo ")
n3=input("Digite o nome de mais um primo ")
n4=input("Digite o nome de mais um primo ")
n5=input("Digite o nome de mais um primo ")
n6=input("Digite o nome de mais um primo ")
n7=input("Digite o nome de mais um primo ")
lista =[n1,n2,n3,n4,n5,n6,n7]
print(f"O melhor primo é {choice(lista)}")
##################################
a=float(input('Digite o valor de um lado do triângulo '))
b=float(input('Digite um  valor de outro lado do triangulo '))
c=float(input('Digite o ultimo valor do triangulo '))
m=max(a,b,c)
import colorama
if a+b+c-m<=m:
    print(f'{colorama.Fore.RED} {colorama.Back.GREEN}os valores não formam triangulo {colorama.Style.RESET_ALL}')
else:
    print(f'os valores podem formar triangulo')

################################################
print('Calcula a sequencia de Fibonacci')
print(f'{"===="*10}')
n=int(input("até que numero você quer a sequencia"))
u=1
p=0
print(p, end=' ')
print(u, end=' ')
acu = u + p
cont=3
while cont<=n:
        print(acu,end=' ')
        p=u
        u=acu
        acu=u+p
        cont+=1
