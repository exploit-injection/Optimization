from sympy import *


def fx1(x1, x2):
    return 5 * pow((x1 - 7), 2) + 5.3 * pow((x2 - 4), 2)


def gradient(x_1, x_2):
    x1 = Symbol('x1')
    x2 = Symbol('x2')
    y = fx1(x1, x2)
    y_x1 = y.diff(x1)  # Производная по x1
    y_x2 = y.diff(x2)  # Производная по x2
    res_x1 = y_x1.evalf(subs={x1: x_1})  # Вычисление производной по x1
    res_x2 = y_x2.evalf(subs={x2: x_2})  # Вычисление производной по x2
    return res_x1, res_x2


def point(x1, x2):
    return x1, x2


def Ovr():
    # Шаг 1 - Задать начальные параметры
    t1 = 0.01  # шаг 1-го этапа
    t2 = 0.1  # шаг 2-го этапа
    e1 = 5.1  # для проверки условий на 1-ом этапе
    e2 = 50  # для проверки условий на 2-ом этапе
    epsilon = 0.001
    N_all = 3  # кол-во циклов
    x0 = point(1, 1)
    stop = (5, 5)  # точка останова
    iteration_first = 1  # для вывода итераций на 1-ом этапе
    iteration_second = 1  # для вывода итераций на 2-ом этапе
    iteration_all = 0  # для подсчета циклов
    iter_count = 0  # для подсчета итераций
    # Шаг 2 - Определить градиент функции gradient()
    # Шаг 3 - Этап 1
    t = t1
    # Шаг 4 - Определяем G(x0)
    G1_x0 = (7, 7)
    while abs(stop[0]) > epsilon and abs(stop[1]) > epsilon and N_all != 0:
        N1 = 7  # кол-во итераций для 1-го этапа
        N2 = 5  # кол-во итераций для 2-го этапа
        print("\n№ цикла:", iteration_all+1)
        print("1 Этап")
        while G1_x0 != (0, 0) and N1 != 0:
            print("\n№ итерации:", iteration_first)
            diff_x0 = gradient(x0[0], x0[1])
            if abs(diff_x0[0]) > e1:
                g1_x0 = diff_x0[0]
            else:
                g1_x0 = 0
            if abs(diff_x0[1]) > e1:
                g2_x0 = diff_x0[1]
            else:
                g2_x0 = 0
            G1_x0 = g1_x0, g2_x0
            print("G1_x = ", G1_x0)
            x1 = x0[0] - t * G1_x0[0], x0[1] - t * G1_x0[1]
            print(f"Значение на 1-ом этапе x{iteration_first} =", x1)
            fx = fx1(x1[0], x1[1])
            print("Значение функции fx =", fx)
            x0 = x1
            N1 = N1 - 1
            iteration_first = iteration_first + 1
            iter_count = iter_count + 1
        else:
            G2_x0 = (5, 5)
            print("Завершение 1-го этапа")
            iteration_first = 1
            print("Результирующее значение на 1-ом этапе x =", x0)
            # Шаг 5 - 2-ой этап
            print("\n2 Этап")
            t = t2
            while G2_x0 != (0, 0) and N2 != 0:
                print("\n№ итерации:", iteration_second)
                diff2_x0 = gradient(x0[0], x0[1])
                # Поиск G2(x0)
                if abs(diff2_x0[0]) < e2:
                    g1_x0 = diff2_x0[0]
                else:
                    g1_x0 = 0
                if abs(diff2_x0[1]) < e2:
                    g2_x0 = diff2_x0[1]
                else:
                    g2_x0 = 0
                G2_x0 = g1_x0, g2_x0
                print("G2_x = ", G2_x0)
                x2 = x0[0] - t * G2_x0[0], x0[1] - t * G2_x0[1]
                print(f"Значение на 2-ом этапе x{iteration_second} =", x2)
                fx2 = fx1(x2[0], x2[1])
                print("Значение функции fx =", fx2)
                x0 = x2
                N2 = N2 - 1
                iteration_second = iteration_second + 1
                iter_count = iter_count + 1
            else:
                print("Завершение 2-го этапа")
                iteration_second = 1
        N_all = N_all - 1
        stop = gradient(x0[0], x0[1])
        iteration_all = iteration_all + 1
    else:
        x_min = x0
        fx_min = fx1(x_min[0], x_min[1])
        print("\nМинимальное значение x = ", x_min)
        print("Минимальное значение функции fx = ", fx_min)
        print("Значение точки останова = ", stop)
        print("Количество циклов = ", iteration_all)
        print("Количество итераций в цикле = ", iter_count)
        print("Завершение работы программы.")


if __name__ == "__main__":
    print("\nМетод Гельфанда-Цейтлина")
    Ovr()
