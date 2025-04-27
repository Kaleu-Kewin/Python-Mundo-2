# quantas pessoas sao maiores de idade

from datetime import date

maioridade = 0
ano_atual  = date.today().year

for i in range(0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - nasc
    
    if idade >= 18:
        maioridade = maioridade + 1
        
print(f'{maioridade} pessoas são maior de idade')