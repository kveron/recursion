from fractal_images import *
from simple_recursion import *


class App:
    print("Выберите функцию:")
    print("1: n-ное число Фибоначчи")
    print("2: максимальное число в заданном списке")
    print("3: список чисел от a до b")
    print("4: Кривая Дракона")
    print("5: Папоротник Барнсли")
    variation = int(input(""))

    if variation == 1:
        print("Введите число:")
        n = int(input(""))
        print("n-ное число Фибоначчи:")
        print(find_fibonacci(n))

    elif variation == 2:
        n = []
        print("Введите длину листа:")
        length = int(input(""))
        print("Введите числа:")
        for i in range(length):
            n.append(int(input("")))
        print("Максимальное число:")
        print(maximum(n))

    elif variation == 3:
        print("Введите a:")
        a = int(input(""))
        print("Введите b:")
        b = int(input(""))
        print(from_a_to_b(a, b))

    elif variation == 4:
        print("Введите число итераций:")
        n = int(input(""))
        DragonCurve.draw_dragon(n)
        print("Фрактал сохранен в fractal.png")

    elif variation == 5:
        print("Введите число итераций:")
        n = int(input(""))
        image = BarnsleyFern.draw_barnsley_fern(n)
        print("Фрактал сохранен в fractal.png")

    else:
        print("Неверное значение")


image.save("fractal.png", "PNG")
