# Melhoria ex 61

razao = int(input('Digite a razão da PA: '))

pa = []
qtde = 10
termos = razao

while qtde != 0:
    for _ in range(qtde):
        pa.append(termos)
        termos = termos + razao

    print(pa)
    print(f'{len(pa)} termos exibidos.')
    
    qtde = int(input('Deseja exibir mais quantos termos? (0 para sair): '))

print('Programa finalizado.')