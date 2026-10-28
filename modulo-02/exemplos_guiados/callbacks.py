def aplicar(funcao, valores):
    return [funcao(v) for v in valores]

def dobro(x):
    return x * 2

print(aplicar(dobro, [1, 2, 3]))
print(aplicar(str.capitalize, ["Ana", "Bia"]))