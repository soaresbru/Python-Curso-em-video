def leiaint(a):
    while True:
        try:
            b=int(a)
            return b
        except:
            print('Erro não é número inteiro')
            a=input('digite um novo valor')

def leiareal(c):
    while True:
        try:
            d=float(c)
            return d
        except:
            print('Erro digite um número real')
            c=input('Digite um número real')

m=input('Digite um número inteiro ')

k=leiaint(m)
n=input('Digite um número real ')
l=leiareal(n)
print(f'o número inteiro é {k} e o real é o {l}')
