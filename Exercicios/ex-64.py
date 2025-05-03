# ler varios numeros e etc

soma = 0
numeros = []

while True:
    numero = int(input('Digite um número. "999" para parar: '))
    
    if numero == 999:
        print('Finalizando programa..')
        break
    
    numeros.append(numero)
    soma = soma + numero
    
print(f'Os numeros digitados foram: {numeros}')
print(f'A soma dos números foi: {soma}')