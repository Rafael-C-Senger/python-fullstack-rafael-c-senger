saldo = 150.0
valor = 150.0

if valor < saldo:
    saldo -= valor
    print("Compra aprovada")
elif valor == saldo:
    saldo -= valor
    print("Valor igual ao saldo!")
else:
    print("Saldo insuficiente")
print(f"Saldo: R$ {saldo:.2f}")