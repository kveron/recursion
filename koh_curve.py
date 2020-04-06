#!/usr/bin/env python
import math
from PIL import Image, ImageDraw


class Point:  # Просто точка с двумя координатами
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def distance(start: Point, end: Point):
    """
    Возвращает растояние между двумя точками. Считает по формуле Пифагора
    """
    dx = start.x - end.x
    dy = start.y - end.y
    return math.sqrt(dx ** 2 + dy ** 2)


def draw_kohs_line(start: Point, end: Point, draw: ImageDraw.ImageDraw):
    length = distance(start, end)
    if length < 5:
        # Если расстояние между двумя точками меньше заданной точночти, то просто рисуем прюмую линию
        draw.line((int(round(start.x)), int(round(start.y)), int(round(end.x)), int(round(end.y))))
    else:
        # Иначе, делим ее на 3 части и рисуем 4 линии Коха рекурсивно

        # Находим вторую точку. Она находится на расстоянии 1/3 длины линии от начальной точки

        point2_x = start.x + (end.x - start.x) / 3
        point2_y = start.y + (end.y - start.y) / 3
        point2 = Point(point2_x, point2_y)

        # Находим координаты третьей точки. Эта точка находится на 60 градусов(math.pi/3)
        # левее от второй точки на расстоянии 1/3 длины линии

        # Угол основной линии находим с помощью арктангенса
        line_angle = math.atan((start.y - end.y) / (end.x - start.x))
        if end.x < start.x:
            line_angle += math.pi
        point3_angle = line_angle + math.pi / 3
        point3_x = point2_x + math.cos(point3_angle) * length / 3
        point3_y = point2_y - math.sin(point3_angle) * length / 3
        point3 = Point(point3_x, point3_y)

        # Находим четвертую точку. Она находится на расстоянии 2/3 длины линии от начальной точки

        point4_x = start.x + 2 * (end.x - start.x) / 3
        point4_y = start.y + 2 * (end.y - start.y) / 3
        point4 = Point(point4_x, point4_y)

        # Рисуем еще 4 линии Коха

        draw_kohs_line(start, point2, draw)
        draw_kohs_line(point2, point3, draw)
        draw_kohs_line(point3, point4, draw)
        draw_kohs_line(point4, end, draw)


if __name__ == "__main__":
    width, height = 1200, 400

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.ImageDraw(image)

    start_point = Point(0, height - 40)
    end_point = Point(width, height - 40)
    draw_kohs_line(start_point, end_point, draw)

    image.save("koh_curve.png")
    image.show()
