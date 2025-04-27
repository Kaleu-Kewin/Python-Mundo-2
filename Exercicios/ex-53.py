# verifica palindromo

# sofri um pouco pra fazer esse

palavra = input('Verificar palavra palindromo: ').replace(' ', '').lower()
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - i - 1]:
        print('não é palindromo')
        break
else:
    print('é palindromo')