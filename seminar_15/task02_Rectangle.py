# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним
# логирование ошибок и полезной информации. Также реализуйте возможность
# запуска из командной строки с передачей параметров.

import argparse
import logging


FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, filename='logs_for_Rectangle.log', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width: int, height=None):
        self.log = logging.getLogger("logs_for_Rectangle.log")
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--width', type=int, help="Ширина", default=5)
    parser.add_argument('-he', '--height', type=int, help="Высота", default=5)
    args = parser.parse_args()
    try:
        Rectangle(args.width, args.height)
    except NegativeValueError as err:
        print("Ошибка NegativeValueError")
        logging.error(f"{args.width} / {args.height} : Ширина и высота должны быть положительными")
    print(Rectangle)
