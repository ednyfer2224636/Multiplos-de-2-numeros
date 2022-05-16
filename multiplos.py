"""Leer 2 números enteros y ver si uno es múltiplo del otro"""

x=int(input("Digite el primer número entero: "))
y=int(input("Digite el segundo número entero: "))

z=float(x % y)

if x < y:
    print(x, "no puede ser múltiplo de", y)
else: 
    if z == 0:
        print(x, "es múltiplo de", y)
    else:
        print(x, "no es múltiplo de", y)