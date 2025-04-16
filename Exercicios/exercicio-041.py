from datetime import datetime

print('--- Natação ---')

nascimento = input('Digite sua data de nascimento (DD/MM/YYYY): ')
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

hoje = datetime.strptime('15/04/2025', '%d/%m/%Y')

idade = nascimento - hoje

print(idade) 

# Não consegui