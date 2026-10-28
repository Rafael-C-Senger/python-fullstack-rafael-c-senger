def imc(peso: float, altura: float) -> float:
    """ 
    Calcula o IMC de uma pessoa

    Arg: 
        - peso: em Kg
        - altura: em m        
    """
    return peso / altura ** 2

print(round(imc(60, 1.80), 2))
