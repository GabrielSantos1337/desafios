import math

print("Insira um valor")

valor = int(input())

if(valor >= 0):
    print("O número {} ao quadrado é: {}" .format(valor, (valor ** 2)))
    print("A raiz quadrada do número {} é {}" .format(valor, math.sqrt(valor)))
else:
    print("O número {}, é invalido" .format(valor))