idade = -5
try:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    print("Idade válida")
except ValueError as e:
    print(f"Erro: {e}")