from __future__ import annotations
import math
from typing import Tuple, Union

from multipledispatch import dispatch


class Point:
    @dispatch(tuple)
    def __init__(self, point_tuple: Tuple[int, int]):
        self.x: int = point_tuple[0]
        self.y: int = point_tuple[1]

    @dispatch(int, int)
    def __init__(self, point_x: int, point_y: int):
        self.__init__((point_x, point_y))

    @dispatch()
    def __init__(self):
        self.__init__((0, 0))

    @property
    def value(self) -> Tuple[int, int]:
        return self.x, self.y

    @value.setter
    def value(self, val: Tuple[int, int]):
        self.x = val[0]
        self.y = val[1]

    def __str__(self) -> str:
        return 'Point({0}, {1})'.format(self.x, self.y)

    @property
    def len(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __add__(self, other: Point) -> Point:
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other: Point) -> Point:
        return Point((self.x - other.x, self.y - other.y))


class Dimension:
    @dispatch(tuple)
    def __init__(self, dimension_tuple: Tuple[int, int]):
        self.width: int = dimension_tuple[0]
        self.height: int = dimension_tuple[1]

    @dispatch(int, int)
    def __init__(self, width: int, height: int):
        self.__init__((width, height))

    @dispatch(Point)
    def __init__(self, point: Point):
        self.__init__(point.value)

    @dispatch()
    def __init__(self):
        self.__init__((0, 0))

    @property
    def value(self) -> Tuple[int, int]:
        return self.width, self.height

    @value.setter
    def value(self, val: Tuple[int, int]):
        self.width = val[0]
        self.height = val[1]

    def __str__(self) -> str:
        return 'Dimension({0}, {1})'.format(self.width, self.height)


class Vector2D:
    """
    Class to represent 2-dimensional vector and related operations
    """
    @dispatch(tuple)
    def __init__(self, vector_tuple: Tuple[float, float]):
        self.x: float = vector_tuple[0]
        self.y: float = vector_tuple[1]

    @dispatch(float, float)
    def __init__(self, vector_x: float, vector_y: float):
        self.__init__((vector_x, vector_y))

    @dispatch(Point)
    def __init__(self, point: Point):
        self.__init__(point.value)

    @dispatch(Point, Point)
    def __init__(self, src_point: Point, dest_point: Point):
        self.__init__(dest_point - src_point)

    @dispatch()
    def __init__(self):
        self.__init__((0, 0))

    @property
    def len(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    @property
    def normalized(self) -> Vector2D:
        """
        Returns unit vector
        @return: unit_vector (Vector2D)
        """
        _len: float = self.len
        return Vector2D() if _len == 0 else self.__truediv__(_len)

    @property
    def value(self) -> Tuple[float, float]:
        return self.x, self.y

    @value.setter
    def value(self, val: Tuple[float, float]):
        self.x = val[0]
        self.y = val[1]

    def __str__(self) -> str:
        return 'Vector2D({0}, {1})'.format(self.x, self.y)

    def __pos__(self) -> Vector2D:
        return Vector2D((self.x, self.y))

    def __neg__(self) -> Vector2D:
        return Vector2D((-self.x, -self.y))

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D((self.x + other.x, self.y + other.y))

    def __iadd__(self, other: Vector2D) -> Vector2D:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D((self.x - other.x, self.y - other.y))

    def __isub__(self, other: Vector2D) -> Vector2D:
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, operand: Union[int, float, Vector2D]) -> Union[Vector2D, float]:
        if type(operand) is int or type(operand) is float:
            return Vector2D((self.x * operand, self.y * operand))
        else:
            return self.x * operand.x + self.y * operand.y

    def __imul__(self, scalar: Union[int, float]) -> Vector2D:
        self.x *= scalar
        self.y *= scalar
        return self

    def __truediv__(self, scalar: Union[int, float]) -> Vector2D:
        if scalar == 0:
            raise ZeroDivisionError
        else:
            return Vector2D((self.x / scalar, self.y / scalar))

    def __idiv__(self, scalar: Union[int, float]) -> Vector2D:
        if scalar == 0:
            raise ZeroDivisionError
        else:
            self.x /= scalar
            self.y /= scalar
            return self

    def __floordiv__(self, scalar: Union[int, float]) -> Vector2D:
        if scalar == 0:
            raise ZeroDivisionError
        else:
            return Vector2D((self.x // scalar, self.y // scalar))

    def __ifloordiv__(self, scalar: Union[int, float]) -> Vector2D:
        if scalar == 0:
            raise ZeroDivisionError
        else:
            self.x //= scalar
            self.y //= scalar
            return self

    def decompose(self, direction: Vector2D) -> Tuple[Vector2D, Vector2D]:
        _unit_direction = direction.normalized

        parallel_component = _unit_direction.__mul__(self * _unit_direction)
        perpendicular_component = self.__sub__(parallel_component)

        return parallel_component, perpendicular_component
