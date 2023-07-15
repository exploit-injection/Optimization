import sympy as sym
from sympy import *


def fx1(x1, x2):
    return (x1 - 2) ** 2 + (x2 - 4) ** 2 + 50 * (x2 + 4 * x1 - 6) ** 2 + 8.3


def gradient(x_1, x_2):
    x1 = Symbol('x1')
    x2 = Symbol('x2')
    y = fx1(x1, x2)
    y_x1 = y.diff(x1)  # Производная по x1
    y_x2 = y.diff(x2)  # Производная по x2
    res_x1 = y_x1.evalf(subs={x1: x_1, x2: x_2})  # Вычисление производной по x1
    res_x2 = y_x2.evalf(subs={x2: x_2, x1: x_1})  # Вычисление производной по x2
    return res_x1, res_x2


def point(x1, x2):
    return x1, x2


def convert_set(sets):
    return sorted(sets)


def Naisk(operation):
    # Шаг 1 - Задать исходные данные

    x0 = point(1869, 3652)  # начальная точка x[0]
    print("x0 = ", x0)
    fx0 = fx1(x0[0], x0[1])
    print("Значение функции в точке x0, fx0 = ", fx0)

    iteration = 1  # итерации для счета
    epsilon = 0.00000001  # точность решения задачи
    diff_fx1 = (5, 5)
    # Шаг 2 - начало итераций
    # Поиск точки x1
    while abs(diff_fx1[0]) > epsilon or abs(diff_fx1[1]) > epsilon:
        print("\n№ итерации: ", iteration)
        grad_x = gradient(x0[0], x0[1])  # определяем значения в градиенте подставляя x0
        t0_sym = Symbol('t0')
        x1 = x0[0] - grad_x[0] * t0_sym, x0[1] - grad_x[1] * t0_sym  # вычисление x[1]
        phi_x = operation(x1[0], x1[1])
        diff_phi_x = phi_x.diff(t0_sym)  # Производная по t0
        t0_mn = sym.solveset(diff_phi_x, t0_sym)  # Найденное значение t0 представлено множеством
        t0_result = convert_set(t0_mn)
        x1_result = x0[0] - t0_result[0] * grad_x[0], x0[1] - t0_result[0] * grad_x[1]  # Вычисленное значение x1
        print("Значение функции phi_x = ", phi_x)
        print("Производная по t =", diff_phi_x)
        print(f"Значение шага t на {iteration} итерации = ", t0_result[0])
        print(f"Значение x на {iteration} итерации = ", x1_result)
        fx = fx1(x1_result[0], x1_result[1])
        print("Значение функции fx =", fx)

        # Шаг 3 - Подстановка значений x1 в градиент для проверки условия останова
        diff_fx1 = gradient(x1_result[0], x1_result[1])
        print("Значение точек останова =  ", abs(diff_fx1[0]), ", ", abs(diff_fx1[1]))

        # Шаг 4 - Проверка условия останова
        if abs(diff_fx1[0]) < epsilon and abs(diff_fx1[1]) < epsilon:
            print("\nМинимальное значение x = ", x1_result)
            fx_min = fx1(x1_result[0], x1_result[1])
            print("Минимальное значение функции = ", fx_min)
            print("Значение точек при проверки условия останова = ", diff_fx1)
            print("Выполнение программы завершено.")
        else:
            x0 = x1_result
            iteration = iteration + 1


if __name__ == "__main__":
    print("\nНаискорейший спуск\n")
    Naisk(fx1)
