def find_fibonacci(n):
    if n in (1, 2):
        return 1
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)


def from_a_to_b(a, b, numbers=[]):
    if a > b:
        return "a must be less than b"  # заменил print ради тестов
    numbers.append(a)
    if a < b:
        numbers = from_a_to_b(a + 1, b, numbers)
    return numbers


def maximum(list_of_numbers, maxi=0):
    number = list_of_numbers.pop()
    if maxi < number:
        maxi = number
    if list_of_numbers:
        maxi = maximum(list_of_numbers, maxi)
    return maxi
