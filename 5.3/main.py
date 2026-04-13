"""
Формула Симпсона
"""
import math


def f(x: float) -> float:
    return x * math.sqrt(x + 1)


if __name__ == "__main__":
    print("Введите концы промежутка")
    a = float(input("A = "))
    b = float(input("B = "))
    
    print("Введите N")
    n = int(input("N = "))
    
    h = (b - a) / n
    s = (f(a) - f(b)) / 2
    
    for i in range(1, n // 2 + 1):
        x = a + 2 * i * h
        s += f(x) + 2 * f(x - h)
    
    s *= 2 * h / 3
    
    print(f"Значение интеграла {s}")