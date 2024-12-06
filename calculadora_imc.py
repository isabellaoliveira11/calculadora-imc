# calculadora_imc.py

def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso e altura fornecidos."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com as diretrizes padrão."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
