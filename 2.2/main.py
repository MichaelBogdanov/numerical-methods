"""
Метод Гаусса
"""

N = 4
EPS = 1e-12

# Ввод матрицы коэффициентов A
a = [
    [float(input(f"A({i + 1},{j + 1}) = ")) for j in range(N)]
    for i in range(N)
]

# Ввод вектора свободных членов b
b = [float(input(f"B({i + 1}) = ")) for i in range(N)]


def reverse(k: int, r: int) -> None:
    """Перестановка k-го и r-го уравнений"""
    a[k], a[r] = a[r], a[k]
    b[k], b[r] = b[r], b[k]


def dv(k: int) -> None:
    """Деление k-го уравнения на ведущий элемент a[k][k]"""
    pivot = a[k][k]
    if abs(pivot) < EPS:
        raise ValueError("Нулевой ведущий элемент, деление невозможно")

    for j in range(k, N):
        a[k][j] /= pivot
    b[k] /= pivot


def clear(k: int, r: int) -> None:
    """Исключение из r-го уравнения переменной x[k]"""
    factor = a[r][k]
    for j in range(k, N):
        a[r][j] -= factor * a[k][j]
    b[r] -= factor * b[k]


if __name__ == "__main__":
    # Прямой ход
    for k in range(N):
        # Если ведущий элемент слишком мал — ищем строку для перестановки
        if abs(a[k][k]) < EPS:
            i = k + 1
            while i < N and abs(a[i][k]) < EPS:
                i += 1
            if i == N:
                raise ValueError("Система не имеет единственного решения")
            reverse(k, i)

        # Нормируем k-ю строку
        dv(k)

        # Обнуляем элементы ниже ведущего
        for i in range(k + 1, N):
            clear(k, i)

    # Обратный ход
    x = [0.0] * N
    for i in range(N - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, N):
            x[i] -= a[i][j] * x[j]
        # так как после dv диагональный элемент равен 1

    # Вывод ответа
    print("Решение системы:")
    for i in range(N): 
        print(f"x{i + 1} = {x[i]}")
