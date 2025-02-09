def circle_area(r):
    """Вычисление площади круга"""
    S  = 3.14159 * r ** 2
    return S


def square_area(side):
    """Вычисление площади квадрата"""
    return side ** 2


def rectangle_area(length, width):
    """Вычисление площади прямоугольника"""
    return length * width


def trapezoid_area(base1, base2, height):
    """Вычисление площади трапеции"""
    return ((base1 + base2) / 2) * height


def triangle_area(base, height):
    """Вычисление площади треугольника"""
    return (base * height) / 2


def main():
    print("Выберите фигуру, площадь которой хотите найти:")
    print("1. Круг")
    print("2. Квадрат")
    print("3. Прямоугольник")
    print("4. Трапеция")
    print("5. Треугольник")

    choice = int(input("Ваш выбор (укажите цифру): "))

    if choice == 1:
        radius = float(input("Введите радиус круга: "))
        area = circle_area(radius)
        print(f"Площадь круга с радиусом {radius} равна {area:.2f}")

    elif choice == 2:
        side = float(input("Введите сторону квадрата: "))
        area = square_area(side)
        print(f"Площадь квадрата со стороной {side} равна {area:.2f}")

    elif choice == 3:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = rectangle_area(length, width)
        print(f"Площадь прямоугольника длиной {length} и шириной {width} равна {area:.2f}")

    elif choice == 4:
        base1 = float(input("Введите основание 1 трапеции: "))
        base2 = float(input("Введите основание 2 трапеции: "))
        height = float(input("Введите высоту трапеции: "))
        area = trapezoid_area(base1, base2, height)
        print(f"Площадь трапеции с основаниями {base1}, {base2} и высотой {height} равна {area:.2f}")

    elif choice == 5:
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = triangle_area(base, height)
        print(f"Площадь треугольника с основанием {base} и высотой {height} равна {area:.2f}")

    else:
        print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()