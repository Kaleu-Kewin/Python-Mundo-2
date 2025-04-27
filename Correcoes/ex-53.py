# Palindromo sem usar FOR

frase    = str(input('Frase: '))
palavras = frase.split()
junto    = ''.join(palavras)
inverso  = junto[::-1]

print(f'O Inverso de {junto} é {inverso}')

if junto == inverso:
    print('É Palindromo!')
else:
    print('Não é Palindromo!')