# Aprovar Empréstimo Bancário

print('--- Faça seu empréstimo bancário! ---')

casa  = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário?: '))
tempo = float(input('Em quantos anos pretende pagar?: '))

mensal = casa / (tempo * 12)

validar = (salario * 30) / 100

if mensal > validar:
    print('O empréstimo ultrapassou 30% do salário. Empréstimo negado!')
else:
    mensal = str(mensal)
    print('Você vai pagar R$ {} por mês!'.format(mensal))