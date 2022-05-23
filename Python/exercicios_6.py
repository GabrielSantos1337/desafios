print("Insira dois valores")

valorX = int(input())
valorY = int(input())

if(valorX > valorY):
    print("O número {} é maior que o número {}" .format(valorX, valorY))
else:
    print("O número {} é maior que o número {}" .format(valorY, valorX))

diferenca = valorX - valorY

print(diferenca)
