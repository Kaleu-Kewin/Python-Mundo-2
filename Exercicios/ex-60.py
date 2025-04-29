# Fatorial de um número

n = int(input('Digite um número: '))
f = 1

cont = n

while cont > 1:
    f = f * cont
    cont = cont - 1

print(f"O fatorial de {n} é {f}")