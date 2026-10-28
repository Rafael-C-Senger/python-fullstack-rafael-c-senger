COMANDOS = {}

def comando(nome):
    def registrar(funcao):
        COMANDOS[nome] = funcao
        return funcao
    return registrar

@comando("oi")
def saudar():
    return "Ola!"

@comando("tchau")
def despedir():
    return "Até logo!"

print(COMANDOS["oi"](), COMANDOS["tchau"]())
print(COMANDOS)