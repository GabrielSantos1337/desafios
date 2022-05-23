import math
print("Leia um número")

valor = int(input())

if(valor < 0):
    print("O valor é inválido.")
else:
    print("A raiz quadrada de {} é {}" .format(valor, math.sqrt(valor)))
