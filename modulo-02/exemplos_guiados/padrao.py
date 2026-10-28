import random
from datetime import date
from collections import Counter

random.seed(7)
print(random.randint(1,6), random.choice(["Ana", "Bia", "Caio"]))
print((date(2026, 12, 25) - date(2026, 10 ,19)).days)
print(Counter("banana"))