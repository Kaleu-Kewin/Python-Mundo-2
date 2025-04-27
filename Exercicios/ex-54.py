# quantas pessoas sao maiores de idade

from datetime import date

maior = 0
menor = 0

ano_atual = date.today().year

for i in range(0, 7):
    nasc  = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - nasc
    
    if idade >= 18:
        maior += 1
    else:
        menor += 1
        
print(f'{maior} pessoas são maior de idade e {menor} são menor de idade')