class Shape:
    def __init__(self, area) -> None:
        self.area = area

    def validate_area(self, area):
        if not isinstance(area, (float, int)):
            raise ValueError("Area must be a number")

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.validate_area(area)
        self.__area = area

    def __eq__(self, other):
        return other.area == self.area

    def __hash__(self):
        return hash(self.area)


shape1 = Shape(100)
shape2 = Shape(100)
shape3 = Shape(150)

# Сравнение фигур
print(shape1 == shape2)  # True
print(shape1 == shape3)  # False

# Использование в словаре
shape_dict = {shape1: "Square", shape3: "Circle"}
print(shape_dict[shape2])  # "Square", т.к. shape1 и shape2 считаются одинаковыми
