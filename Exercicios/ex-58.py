# Acertar o numero gerado pela maquina, exibir pergunta ate acertar

from random import randint

aleatorio = randint(1, 10)

n = int(input('Adivinhe o numero entre 1 e 10: '))

while n != aleatorio:
    n = int(input('Errado! Tente novamente: '))
    
    if (n == aleatorio):
        print('Acertou!')