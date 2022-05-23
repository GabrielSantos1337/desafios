print("Insira dois valores")

X = int(input())
Y = int(input())

if(X > Y):
    print("O número {} é maior" .format(X))
elif(Y > X):
    print("O número {} é maior" .format(Y))
else:
    print("Números iguais")
