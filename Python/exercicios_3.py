import math

print("Insira um número: ")

valor = int(input())

if(valor >= 0):
    print("O seu número é positivo, portanto, a raiz quadra de {} é: {}" .format(valor, math.sqrt(valor)))
else:
    print("{} ao quadrado é {}" .format(valor, (valor ** 2)))
