# Aplicar desconto 

print('--- Desconto ---')

preco = float(input('Qual o valor do produto?: '))

print('Escolha uma forma de pagamento: ')
print('1. Dinheiro / Cheque')
print('2. Cartão')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    preco = preco - (preco * 0.10)
    print('Desconto de 10% Aplicado! Valor final do produto: R$ {}'.format(preco))

if opcao == 2:
    qtd = int(input('Em quantas vezes deseja pagar?: '))

    if qtd > 2:
        preco = preco + (preco * 0.20)
        print('Juros de 20% Aplicado! Valor final do produto: R$ {}'.format(preco))