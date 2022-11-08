
n=int(input('Diga um número inteiro que você quer converter '))
c=int(input('escolha digitando o número de qual base de conversão você quer:'
            ' \n [1] binario'
            '\n [2] octal'
            '\n [3] hexadecimal '
            '\n'))
if c==1:
    print(f'o número é {bin(n)[2:]} ')
elif c==2:
    print(f'o número é {oct(n)[2:]}')
elif c==3:
    print(f'O número é {hex(n)[2:]}')
else:
    print(f'a opção {c} não existe, tente outra opção')
