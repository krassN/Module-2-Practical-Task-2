first = int(input('Введите число 1 : '))
second = int(input('Введите число 2 : '))
third = int(input('Введите число 3 : '))
if first == second and first != third and second != third:
    print(2)
elif first == third and first != second and third != second:
    print(2)
elif second == third and second != first and third != first:
    print(2)
elif first == second == third:
    print(3)
elif first != second != third:
    print(0)
