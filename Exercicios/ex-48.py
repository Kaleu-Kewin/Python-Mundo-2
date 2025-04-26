# Somar numeros impares que são multiplos de 3 entre 1 e 500

soma = 0

for i in range(1, 500):
    if (i % 2 != 0) and (i % 3 == 0): 
        print(f'Números ímpares e múltiplos de 3 entre 1 e 500: {i}')
        soma = soma + i  

print(f'A soma dos números é: {soma}')
