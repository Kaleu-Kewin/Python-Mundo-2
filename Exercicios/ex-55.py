# maior e menor peso

pesos = []

for i in range(0, 5):
    p = float(input('Digite seu peso: '))
    pesos.append(p)
    
maior = max(pesos)
menor = min(pesos)

print(f'\nMaior peso: {maior}')
print(f'Menor peso: {menor}')