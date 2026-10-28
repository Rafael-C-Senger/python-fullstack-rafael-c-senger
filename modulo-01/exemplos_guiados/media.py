n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
media = (n1 + n2 + n3)/3
print(f"Média: {media:.2f}")
print(f"Aprovado? {media >= 7}")
print(f"Recuperação? {5 <= media < 7}")
