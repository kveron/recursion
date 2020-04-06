from simple_recursion import *


def test(n, x, y):
    if x == y:
        print(str(n) + " тест прошел успешно")
    else:
        print(str(n) + " тест провален")


class Repo:
    @staticmethod
    def make_tests():
        test(1, maximum([92, 1, 2, 3, 4, 5, 6, 9, 11, 17, 0, 2, 7, 49, -17]), 92)
        test(2, maximum([-347, 92, 192, 33, 64]), 192)
        test(3, maximum([1, 2, 3, 4, 5, 6, 0, 10, 11, 11, 9, -9999999]), 11)
        test(4, maximum([10, 9, 8, 3, 6]), 10)
        test(5, maximum([192]), 192)

        test(6, from_a_to_b(0, 20, []), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        test(7, from_a_to_b(-9, 5, []), [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
        test(8, from_a_to_b(-117, -9, []),
             [-117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101,
              -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80,
              -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59,
              -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38,
              -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17,
              -16, -15, -14, -13, -12, -11, -10, -9]
             )
        test(9, from_a_to_b(-3, 3, []), [-3, -2, -1, 0, 1, 2, 3])
        test(10, from_a_to_b(5, 0, []), "a must be less than b")
        test(11, fib(9), 34)
        test(12, fib(30), 832040)
        test(13, fib(1), 1)
        test(14, fib(2), 1)
        test(15, fib(3), 2)
