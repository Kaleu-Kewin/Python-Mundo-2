# Calculadora

opcao = 0

while opcao != 5:
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))

    while True:
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos números')
        print('[5] Sair do programa')
        
        opcao = int(input('Escolha uma opção: '))

        match opcao:
            case 1: print(f'A soma dos valores é: {n1 + n2}')
            case 2: print(f'A multiplicação dos valores é: {n1 * n2}')
            case 3: 
                if n1 > n2:
                    print(f'O maior valor é: {n1}')
                elif n2 > n1:
                    print(f'O maior valor é: {n2}')
                else:
                    print('Os valores são iguais.')
            case 4: break
            case 5: 
                print('Encerrando o programa..') 
                exit() 
            case _:
                print('Opção inválida!')