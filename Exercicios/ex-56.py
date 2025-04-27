# Nome, idade e sexo de 4 pessoa + Mostrar a média das idades, o homem mais velho e quantas mulheres têm menos de 20 anos

pessoas = []

soma_idades = 0

mais_velho = {'nome: ': '', 'idade': 0}
menos_20 = 0

for i in range(4):
    dados = input('Digite Nome, Idade e Sexo (F/M), separados por vírgulas: ').split(',')
    
    nome  = dados[0].strip()
    idade = int(dados[1].strip())
    sexo  = dados[2].strip().upper()

    pessoa = {
        'nome'  : nome,
        'idade' : idade,
        'sexo'  : sexo
    }
    
    pessoas.append(pessoa)
    
    soma_idades = soma_idades + idade
    
    if sexo == 'M' and idade > mais_velho['idade']:
        mais_velho['nome'] = nome
        mais_velho['idade'] = idade    
    
    if sexo == 'F' and idade < 20:
    
        menos_20 = menos_20 + 1
    
    media_idades = soma_idades / 4

print(f'\nMédia das idades: {media_idades} anos')
print(f'Homem mais velho: {mais_velho["nome"]} com {mais_velho["idade"]} anos')
print(f'Quantidade de mulheres com menos de 20 anos: {menos_20}')