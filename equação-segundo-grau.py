input("vamos resolver uma equação da forma ax^2+bx+c")
a=float(input("Digite o valor de a"))
b=float(input("Digite o valor de b"))
c=float(input("Digite o valor de c"))

delta=(b**2)-(4*a*c)
d=(delta)**(1/2)
if d>0:
	x1=(-b+d)/2*a
	x2=(-b-d)/2*a
	print("as raizes são",x1," ",x2)
else:
	print("não possui raizes reais")