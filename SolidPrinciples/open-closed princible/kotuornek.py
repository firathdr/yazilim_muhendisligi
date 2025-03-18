from math import pi

def calculate_area(shape):
    if shape["type"] == "circle":
        return pi * shape["radius"] ** 2
    elif shape["type"] == "rectangle":
        return shape["width"] * shape["height"]

circle = {"type": "circle", "radius": 5}
rectangle = {"type": "rectangle", "width": 4, "height": 6}

shapes = [circle, rectangle]
for shape in shapes:
    print(calculate_area(shape))
