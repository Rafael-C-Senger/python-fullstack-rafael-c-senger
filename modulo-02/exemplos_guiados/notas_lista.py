notas = []
for i in range(3):
    notas.append(float(input(f"Nota {i+1}: ")))
print(max(notas), min(notas))
print(f"Média: {sum(notas) / len(notas):.2f}")
print(sorted(notas, reverse=True))