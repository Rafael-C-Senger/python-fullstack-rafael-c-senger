try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: digite um número válido.")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Encerrando operação!")