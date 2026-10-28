taxa = 0.1
def preco_final(preco):
    desconto = preco * taxa
    return preco - desconto
print(preco_final(200))
#print(desconto)
