def check_sign(mas):
    sign = mas[0]
    for elem in mas:
        if elem * sign < 0:
            return False
    return True

mas1 = [float(x) for x in input("Введите элементы массива 1: ").split()]
mas2 = [float(x) for x in input("Введите элементы массива 2: ").split()]
mas3 = [float(x) for x in input("Введите элементы массива 3: ").split()]
mas4 = [float(x) for x in input("Введите элементы массива 4: ").split()]
mas5 = [float(x) for x in input("Введите элементы массива 5: ").split()]
masivi = [mas1, mas2, mas3, mas4, mas5]

for i, mas in enumerate(masivi, start=1):
    if check_sign(mas):
        print(f"Массив {i} имеет элементы одного знака")
    else:
        print(f"Массив {i} имеет элементы разного знака")
