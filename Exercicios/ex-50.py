# Ler 6 numeros inteiros e somar os que são pares

numeros = input('Digite 6 números Separados por Virgula: ')

soma = 0
ignorados = []

for i in numeros.split(','):
    i = int(i.strip())
    if i % 2 == 0:
        soma += i
    else:
        ignorados.append(i)
        
print(f'A soma dos números pares é: {soma}')
print(f'Numeros ignorados: {ignorados}')