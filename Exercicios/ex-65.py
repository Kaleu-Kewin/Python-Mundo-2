# melhoria ex-64, mostrar media, maior e menor valor

numeros = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    
    continuar = input('Deseja continuar? [S/N]: ').upper()
    
    if continuar == 'N':
        break

media = sum(numeros) / len(numeros)

print(f'\nNumeros digitados: {numeros}')
print(f'O Maior valor digitado foi: {max(numeros)}')
print(f'O Menor valor digitado foi: {min(numeros)}')
print(f'A média é: {media}')