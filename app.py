from fractal_image import *
from simple_recursion import *
from tests import Repo


class App:
    print("Выберите функцию:")
    print("1: n-ное число Фибоначчи")
    print("2: максимальное число в заданном списке")
    print("3: список чисел от a до b")
    print("4: Кривая Дракона")
    print("5: Папоротник Барнсли. Не вызывай, подумой (return image нагружает систему ещё сильнее,из-за чего компиляция не завершается, вызывать лучше из основного файла")
    print("6: Тесты")
    variation = int(input(""))

    if variation == 1:
        print("Введите число:")
        n = int(input(""))
        print("n-ное число Фибоначчи:")
        print(fib(n))

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
        print("Введите число итераций: (идеал - 15)")
        n = int(input(""))
        draw_dragon(n)
        print("Фрактал сохранен в fractal.png")

    elif variation == 5:
        print("Введите число итераций:")
        n = int(input(""))
        barnsley_fern(n)
        print("Фрактал сохранен в fractal.png")

    elif variation == 6:
        Repo.make_tests()

    else:
        print("Неверное значение")
