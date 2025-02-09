def circle_area(r):
    S  = 3.14159 * r ** 2
    return S

# Пример использования функции
radius = float(input("Введите радиус круга: "))
area = circle_area(radius)
print(f"Площадь круга с радиусом {radius} равна {area:.2f}")