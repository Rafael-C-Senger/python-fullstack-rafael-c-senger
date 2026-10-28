def resumo(*notas, **opcoes):
    return max(notas), min(notas), round(sum(notas)/len(notas), opcoes["casas"])

print(resumo(1, 1, 7, 10, 2, 3, 4, 5, casas=2))