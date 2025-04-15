# Ver o maior numero

print('--- Descubra qual o maior valor ---')

n1 = int(input('Digite o primeiro valor: ')) 
n2 = int(input('Digite o segundo valor: '))

if (n1 > n2):
    print('O número {} é o maior!'.format(n1))
elif (n1 == n2):
    print('Os dois números são iguais!')
else:
    print('O número {} é o maior!'.format(n2))