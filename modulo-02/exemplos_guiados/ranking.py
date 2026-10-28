alunos = [("Ana", 9.0),("Beuno", 6.5), ("Carla", 8.0)]
ranking = sorted(alunos, key=lambda a: a[1] ,reverse=True)
print(ranking)