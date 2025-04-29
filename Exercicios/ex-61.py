# razão aritmética usando WHILE (Melhoria do 51)

n  = int(input('Escolha um numero para razão aritmética: '))
pa = []

cont = n

while cont > 0:
    pa.append(cont * n)
    cont = cont - 1
    
print(pa[::-1])