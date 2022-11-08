print('Vamos calcular o número de rebites necessários para o atenuador')
r= str(input('Este atenuador tem veneziana? (S/N) ')).strip().lower()
if r == 'n':
    print('Vamos calcular o número de rebites necessários')
    a = int(input('Qual a largura da peça?'))
    n = a/200
    m = n*4
    r = m+5
    print('O número de rebites necessários é ', r)

    print(" ")
    print('Agora vamos calcular o número de parafusos necessários')
    c = int(input('Qual é o comprimento da peça?'))
    e = int(input('Temos quantas células de até 100 mm?'))
    f = int(input('Temos quantas células de 150 até 200 mm?'))
    g = int(input('Temos quantas células de 300 mm ?'))
    ff = 2*f
    gg = 3*g
    hh = 2*(e+ff+gg)
    cc = c/300
    p = cc * hh
    print('O número de parafusos necessários é', p)
else:
    print('Ainda não sei calcular')
