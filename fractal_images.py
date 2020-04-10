import math

from PIL import Image, ImageColor
from PIL import ImageDraw

width = 4096
height = 4096

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)


class BarnsleyFern:
    @staticmethod
    def draw_barnsley_fern(n, x1=500, y1=3700, angle=60, length=900, angle_for_each_side=3):
        # purple = "rgb("  # попытка сделать градиент, завершившаяся провалом
        # y = 0
        # r = rgb[0]
        # g = rgb[1]
        # b = rgb[2]
        # for i in rgb:
        #     purple += i.__str__()
        #     y += 1
        #     if y < 3:
        #         purple += ","
        # purple += ")"  # не стал пока удалять, может что придумаю
        if n == 0:
            return
        x2 = x1 + int(math.cos(math.radians(angle)) * length)
        y2 = y1 - int(math.sin(math.radians(angle)) * length)
        draw.line((x1, y1, x2, y2), ImageColor.getrgb("rgb(200,0,200)"))
        if length > 3:
            BarnsleyFern.draw_barnsley_fern(n - 1, BarnsleyFern.x_coordinate_for_next_fern(x1, angle, length, 0.6),
                                            BarnsleyFern.y_coordinate_for_next_fern(y1, angle, length, 0.6), angle + 60,
                                            int(round(length * 0.35)), 3)
            BarnsleyFern.draw_barnsley_fern(n - 1, BarnsleyFern.x_coordinate_for_next_fern(x1, angle, length, 0.2),
                                            BarnsleyFern.y_coordinate_for_next_fern(y1, angle, length, 0.2), angle - 60,
                                            int(round(length * 0.4)), -3)
        BarnsleyFern.draw_barnsley_fern(n - 1, x2, y2, angle - angle_for_each_side, int(round(length * 0.8)),
                                        angle_for_each_side)
        return image

    @staticmethod
    def x_coordinate_for_next_fern(x, angle, length, shift):
        x = x + int(round(math.cos(math.radians(angle)) * (length * shift)))
        return x

    @staticmethod
    def y_coordinate_for_next_fern(y, angle, length, shift):
        y = y - int(round(math.sin(math.radians(angle)) * (length * shift)))
        return y


class DragonCurve:
    @staticmethod
    def draw_dragon(n, old=[1], x1=1700, y1=3200, angle=90, length=10):
        new = []
        for i in old:
            new.append(i)
        new.append(1)
        old = old[::-1]
        for i in old:
            if i == 0:
                new.append(1)
            else:
                new.append(0)
        if n > 1:
            DragonCurve.draw_dragon(n - 1, new)
        if n == 1:
            # с помощью рекурсий создаю путь для прямой,
            # а только потом рисую для большей скорости и возможности вызова из app
            for i in new:
                x2 = x1 + int(math.cos(math.radians(angle)) * length)
                y2 = y1 - int(math.sin(math.radians(angle)) * length)
                if i == 1:
                    angle += 90
                else:
                    angle -= 90
                draw.line((x1, y1, x2, y2), ImageColor.getrgb("rgb(255, 0, 0)"))
                x1, y1 = x2, y2
            return image.save("fractal.png", "PNG")
