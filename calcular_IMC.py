def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    if imc <18.5:
        return f'Abaixo do Pesso {imc:.2F} imc'
    elif imc < 25:
        return f'Peso Normal kl:{imc:.2f} imc'
    elif imc <30:
        return f'Voce esta com sobrepeso kl:{imc:.2f} imc'
    else:
        if imc >=30:
            return f'Voce esta com grau! de Obsidade kl:😒 {imc:.2f} imc'
resultado = calcular_imc(85, 1.75)

print(resultado)   