nome, nota = "Ana", 8.5

print("Aluna", nome, sep=": ")
print("Fim", end="!\n")
print(f"{nome} tirou {nota:.1f}")
print(f"{nota * 10:<20.2f}|{1234567:,}")

for i in range(10):
    print(f"{nome:>{i}}")
    