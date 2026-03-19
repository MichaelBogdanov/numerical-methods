"""
Метод касательных (Ньютона)
"""
import math


def f(x: float) -> float:
    return math.exp(x) + 2 * x - 3  # f(x)

def f1(x: float) -> float:
    return math.exp(x) + 2  # f'(x)


if __name__ == "__main__":
    print("Введите концы исходного промежутка")
    a = float(input("A = "))
    b = float(input("B = "))

    print("Введите точность")
    e = float(input("E = "))
    
    print("Введите параметр M")
    m = float(input("M = "))
    
    print("Введите начальное приближение")
    x = float(input("X0 = "))
    
    while abs(f(x)) / m > e:
        x = x - f(x) / f1(x)
    
    print(f"Значение корня с точностью {e} равно {x}")
    print(f"Значение функции f(x) = {f(x)}")
