PI = 3.14159

def area_circulo(raio):
    return PI * raio ** 2

def celsius_para_f(c):
    return c * 9 / 5 + 32

print(__name__)
if __name__ == "__main__":
    print(area_circulo(1))