# O range() pode receber 3 parâmetros: range(início, fim, passo)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):
    print(c)

print('FIM')

# Exemplo de soma com o range()

s = 0

for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n

print('A soma de todos os numeros é {}'.format(s))