def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def from_a_to_b(a, b, numbers=[]):
    if a > b:
        return "a must be less than b"  # заменил print ради тестов
    numbers.append(a)
    if a < b:
        numbers = from_a_to_b(a + 1, b, numbers)
    return numbers


def maximum(list_of_numbers, max=0):
    number = list_of_numbers.pop()
    if max < number:
        max = number
    if list_of_numbers:
        max = maximum(list_of_numbers, max)
    return max
