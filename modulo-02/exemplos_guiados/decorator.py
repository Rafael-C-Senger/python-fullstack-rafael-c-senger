def com_log(funcao):
    def interna(*args, **kwargs):
        print(f"Chamando {funcao.__name__}")
        return funcao(* args, **kwargs)
    return interna

@com_log
def somar(a, b):
    return a + b

@com_log
def sub(a, b):
    return a - b

@com_log
def mult(a, b):
    return a * b

@com_log
def div(a, b):
    return a / b

print(somar(1,3))
print(sub(1,3))
print(mult(1,3))
print(div(1,3))
