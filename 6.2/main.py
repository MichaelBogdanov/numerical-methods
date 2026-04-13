"""
Метод Рунге – Кутта
"""
import math


def f(x: float, y: float) -> float:
    return x * math.exp(-y)


if __name__ == "__main__":
    print("Введите X0")
    x = float(input("X0 = "))
    print("Введите Y0")
    y = float(input("Y0 = "))
    
    # Ввод начальных данных
    print("Введите N")
    n = int(input("N = "))
    print("Введите H")  # шаг
    h = float(input("H = "))
    
    for i in range(0, n + 1):
        print(x, y)  # печать значений: x = x0 + ih, y = y(x)
        
        k1 = f(x, y) * h
        x += h / 2
        
        k2 = f(x, y + k1 / 2) * h
        
        k3 = f(x, y + k2 / 2) * h
        x += h / 2
        
        k4 = f(x, y + k3) * h
        
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
