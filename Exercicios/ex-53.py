# verifica palindromo

# precisei usar gpt nesse, não sabia como fazer

palavra = input('Verificar palavra palindromo: ')
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - i - 1]:
        print('não é palindromo')
        break
else:
    print('é palindromo')