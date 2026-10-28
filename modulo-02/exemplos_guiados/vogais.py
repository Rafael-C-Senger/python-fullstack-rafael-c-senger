frase = input("frase: ").lower()
vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1
print(f"Vogai: {vogais}")