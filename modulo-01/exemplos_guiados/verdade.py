nome = ""
print(bool(nome), bool([]), bool(0), bool("a"))
if not nome:
    print("Nome vazio")
idade = 20
status = "adulto" if idade >= 18 else "menor"
print(status)