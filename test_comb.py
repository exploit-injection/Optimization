import math


def fx(x):
    return (x - 6) * (x - 8) * (x - 4)


def fx_sin(x):
    return x + 6 * math.sin(2.3 * 3.14 * x + 4)


def fx_exp(x):
    return 1 - 6 * math.exp(-pow((x - 6.5) / 4, 2))


def Comb(operation):

    x0 = int(input("Введите значение x0: "))
    delta_x = int(input("Введите значение шага: "))
    epsilon = float(input("Введите точность: "))
    iteration = 1
    fx0 = operation(x0)
    while delta_x > epsilon and iteration < 21:
        print("\n№ итерации:", iteration)
        print("x0 = ", x0)
        print("f(x0) = ", fx0)
        iteration += 1
        x1 = x0 + delta_x
        fx1 = operation(x1)
        if fx1 < fx0:
            x0 = x1
            fx0 = fx1
            delta_x *= 2
        else:
            x2 = x0 - delta_x
            fx2 = operation(x2)

            if fx2 < fx0:
                x0 = x2
                fx0 = fx2
                delta_x *= 2
            else:
                delta_x /= 2
                x3 = x0 + delta_x
                fx3 = operation(x3)
                x4 = x0 - delta_x
                fx4 = operation(x4)
                k = 1

                while fx3 >= fx0 and fx4 >= fx0:
                    delta_x /= 2
                    x3 = x0 + delta_x
                    fx3 = operation(x3)
                    x4 = x0 - delta_x
                    fx4 = operation(x4)
                    k += 1

                if fx3 < fx0:
                    x0 = x3
                    fx0 = fx3
                elif fx4 < fx0:
                    x0 = x4
                    fx0 = fx4

                for i in range(1, k):
                    d = (fx3 - fx4) / (2 * delta_x) + (fx3 - 2 * fx0 + fx4) / (2 * delta_x ** 2) * delta_x
                    if (fx3 - fx0 - d) == 0:
                        x5 = x0
                    else:
                        x5 = x0 - d / (2 * abs((fx3 - fx0 - d) / (fx3 - 2 * fx0 + fx4)))
                    fx5 = operation(x5)

                    if fx5 < fx0:
                        delta_x *= 2
                        x0 = x5
                        fx0 = fx5
                        break

                    if x5 > x0:
                        x4 = x0
                        fx4 = fx0
                    else:
                        x3 = x0
                        fx3 = fx0

                x0 = (x3 + x4) / 2
                fx0 = operation(x0)
                delta_x /= 2

    print("\nРезультат:")
    print("Значение точки x = ", x0)
    print("Минимальное значение функции f(x) = ", fx0)
    print("Количество итераций = ", iteration)



if __name__ == "__main__":
    print("\nКомбинированный метод\n")
    Comb(fx)
    Comb(fx_sin)
    Comb(fx_exp)