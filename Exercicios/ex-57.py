# Continuar exibindo a pergunta até o valor estar correto (M/F)

sexo = input('Digite seu sexo [M/F]: ').upper()

while sexo not in ['M', 'F']:
    sexo = input('Valor inválido. Digite seu sexo [M/F]: ').upper()

match sexo:
    case 'M': print('Sexo masculino registrado com sucesso!')
    case 'F': print('Sexo feminino registrado com sucesso!')     