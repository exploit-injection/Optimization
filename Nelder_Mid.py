import math


def fx1(x1, x2):
    return 5 * pow((x1 - 7), 2) + 5.3 * pow((x2 - 4), 2)


def fx2(x1, x2):
    return (x1 - 2)**2 + (x2 - 4)**2 + 50 * (x2 + 4 * x1 - 6)**2 + 8.3


def point(x1, x2):
    return x1, x2


def Nelder(operation):
    x_easy = (0, 0)
    x_norm = (0, 0)
    x_heavy = (0, 0)
    x_stop = 100
    epsilon = 0.001
    iteration = 1

    #  Шаг1 - Выбор начальных значений
    print("Начальные точки:")
    x1 = point(0, 0)
    # Параметры для 2-ой функции (раскомментировать)
    # t = 6
    # a = (t * (math.sqrt(3) + 2)) / (2 * math.sqrt(2))
    # b = (t * (math.sqrt(3) - 1)) / (2 * math.sqrt(2))
    # x2 = point(a, b)
    # x3 = point(b, a)
    x2 = point(0.97, 0.26)
    x3 = point(0.26, 0.97)
    print("x1 = ", x1)
    print("x2 = ", x2)
    print("x3 = ", x3)

    while x_stop > epsilon:

        print("\n№ итерации: ", iteration)
        # Шаг 2 - Находим значение функции в точках.
        f1 = operation(x1[0], x1[1])
        f2 = operation(x2[0], x2[1])
        f3 = operation(x3[0], x3[1])
        # Определяем тяжелую и легкую точки
        if f1 > f2 > f3:
            x_heavy = x1
            x_norm = x2
            x_easy = x3
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)
        elif f1 > f3 > f2:
            x_heavy = x1
            x_norm = x3
            x_easy = x2
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)
        elif f2 > f1 > f3:
            x_heavy = x2
            x_norm = x1
            x_easy = x3
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)
        elif f2 > f3 > f1:
            x_heavy = x2
            x_norm = x3
            x_easy = x1
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)
        elif f3 > f1 > f2:
            x_heavy = x3
            x_norm = x1
            x_easy = x2
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)
        elif f3 > f2 > f1:
            x_heavy = x3
            x_norm = x2
            x_easy = x1
            print("Тяжелая точка", x_heavy)
            print("Средняя точка", x_norm)
            print("Легкая точка", x_easy)

        # Определяем центр тяжести
        x_center = (0.5 * (x_easy[0] + x_norm[0])), (0.5 * (x_easy[1] + x_norm[1]))
        print("Центр тяжести x_ц = ", x_center)
        fx_center = operation(x_center[0], x_center[1])
        print("fx_center =", fx_center)
        # Определяем точку отражения
        x_otr = (x_center[0] + (x_center[0] - x_heavy[0])), (x_center[1] + (x_center[1] - x_heavy[1]))
        print("Точка отражения x_отр = ", x_otr)

        fx_otr = operation(x_otr[0], x_otr[1])
        f_easy = operation(x_easy[0], x_easy[1])
        f_norm = operation(x_norm[0], x_norm[1])
        f_heavy = operation(x_heavy[0], x_heavy[1])
        print("fx_тяж =", f_heavy)
        print("fx_ср =", f_norm)
        print("fx_лег =", f_easy)
        print("fx_отр =", fx_otr)

        if fx_otr < f_easy:
            print("\nВыполняем растяжение: ")
            # Находим значение точки растяжения
            x_rast = (x_center[0] + 2 * (x_otr[0] - x_center[0])), (x_center[1] + 2 * (x_otr[1] - x_center[1]))
            print("Точка растяжения = ", x_rast)
            fx_rast = operation(x_rast[0], x_rast[1])
            print("fx_раст =", fx_rast)
            if fx_rast < f_easy:
                x_heavy = x_rast
                print("Замена тяжелой точки на точку растяжения.")
                print("Новая тяжелая точка = ", x_heavy)
            else:
                x_heavy = x_otr
                print("Замена тяжелой точки на точку отражения.")
                print("Новая тяжелая точка = ", x_heavy)
        else:
            # Если точка растяжения легче только тяжелой точки
            if fx_otr > f_norm:
                if fx_otr > f_heavy:
                    print("\nВыполняется редукция:")
                    x_heavy = x_easy[0] + 0.5 * (x_heavy[0] - x_easy[0]), x_easy[1] + 0.5 * (x_heavy[1] - x_easy[1])
                    x_norm = x_easy[0] + 0.5 * (x_norm[0] - x_easy[0]), x_easy[1] + 0.5 * (x_norm[1] - x_easy[1])
                    print("Новая тяжелая точка = ", x_heavy)
                    print("Новая средняя точка = ", x_norm)
                else:
                    # Находим точку сжатия
                    x_sg = x_center[0] + 0.5 * (x_center[0] - x_heavy[0]), x_center[1] + 0.5 * (
                                x_center[1] - x_heavy[1])
                    print("\nВыполняется сжатие")
                    print("Точка сжатия x_сж = ", x_sg)
                    fx_sg = operation(x_sg[0], x_sg[1])
                    print("fx_сж =", fx_sg)
                    if fx_sg > f_heavy:
                        x_heavy = x_easy[0] + 0.5 * (x_heavy[0] - x_easy[0]), x_easy[1] + 0.5 * (x_heavy[1] - x_easy[1])
                        x_norm = x_easy[0] + 0.5 * (x_norm[0] - x_easy[0]), x_easy[1] + 0.5 * (x_norm[1] - x_easy[1])
                        print("Новая тяжелая точка = ", x_heavy)
                        print("Новая средняя точка = ", x_norm)
                    else:
                        # Заменяется тяжелая точка на точку сжатия
                        x_heavy = x_sg
                        print("Новая тяжелая точка = ", x_heavy)
            else:
                print("Замена тяжелой точки на точку отражения.")
                x_heavy = x_otr
                print("Новая тяжелая точка = ", x_heavy)

        fx_center = operation(x_center[0], x_center[1])
        fx_easy = operation(x_easy[0], x_easy[1])
        fx_norm = operation(x_norm[0], x_norm[1])
        fx_heavy = operation(x_heavy[0], x_heavy[1])
        x_stop = math.sqrt(
            (0.33 * ((fx_easy - fx_center) ** 2 + (fx_norm - fx_center) ** 2 + (fx_heavy - fx_center) ** 2)))
        print("Значение точки останова = ", x_stop)

        # Проверка условия останова
        if x_stop < epsilon:
            x_min = x_easy
            fx_min = operation(x_easy[0], x_easy[1])
            print("\nМинимальное значение x =", x_min)
            print("Минимальное значение функции = ", fx_min)
            print("Кол-во итераций: ", iteration)
            print("Выполнение программы завершено.")
        else:
            x1 = x_easy
            x2 = x_norm
            x3 = x_heavy
            iteration = iteration + 1


if __name__ == "__main__":
    print("\nМетод Нелдера-Мида\n")
    Nelder(fx1)
    # Nelder(fx2)  #  Расскомментировать для 2-ой функции
