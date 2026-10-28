peso_max = 850
peso_caixa = 32

print(f"A quantidade máxima de caixas que pesam {peso_caixa} kg em um caminhão que supoerta {peso_max} kg é {peso_max//peso_caixa}")
print(f"O peso restante disponível é: {peso_max%peso_caixa} kg")