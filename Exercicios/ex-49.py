# Tabuada usando loop for

n = int(input('Tabuada do: '))

for i in range(1, 10 + 1):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')