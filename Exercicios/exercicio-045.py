# Jokenpo

import random

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('--- Jokenpo ---')
print('1. Pedra')
print('2. Papel')
print('3. Tesoura')

usuario = int(input('Escolha uma opção: ')) - 1  
maquina = random.choice([0, 1, 2])  

print(f'Você escolheu: {opcoes[usuario]}')
print(f'A máquina escolheu: {opcoes[maquina]}')

if usuario == maquina:
    print('Empate!')
elif (usuario == 0) and (maquina == 2) or (usuario == 1) and (maquina == 0) or (usuario == 2) and (maquina == 1):
    print('Você venceu!')
else:
    print('A máquina venceu!')
