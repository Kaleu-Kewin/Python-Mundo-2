# Calcular IMC

print('--- Calculo do IMC ---')

peso   = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (M): '))

imc = peso / (altura ** 2)

def calcularIMC(imc) -> str:
    if imc < 18.5:
        return('Abaixo do peso!')
    elif imc < 25:
        return('Peso ideal!')
    elif imc < 30:
        return('Sobrepeso!')
    elif imc < 40:
        return('Obesidade!')
    elif imc > 40:
        return('Obesidade Mórbida!')
 
resultado = f'Seu IMC é: {imc}. Que significa: ' + calcularIMC(imc)
print(resultado)