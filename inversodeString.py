n=str(input('Digite um frase é descoubra se é palindromo')).upper().strip()
s=n.split()
j=''.join(s)
inverso=''
for i in range(len(j)-1, -1,-1):  #ao inves de usar for podia ter usado só inverso=j[::-1]
    inverso+=j[i]
print(inverso)
if inverso==j:
    print(f'{j} ao contrário é {inverso}, logo é palindromo')
else:
    print(f'{j} ao contrario é {inverso}, logo não é palindromo')
