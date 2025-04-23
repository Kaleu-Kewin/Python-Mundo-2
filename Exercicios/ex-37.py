# Converter números inteiros

print('--- Converter números inteiros ---')

print('1. Binario')
print('2. Octal')
print('3. Hexadecimal')

opcao  = int(input('Escolha uma opção: '))
numero = int(input('Digite o número a ser converido..: '))

if opcao == 1:
    result = bin(numero)
    print('Resultado: {}'.format(result))
elif opcao == 2:
    result = oct(numero)
    print('Resultado: {}'.format(result))
elif opcao == 3:
    result = hex(numero)
    print('Resultado: {}'.format(result))