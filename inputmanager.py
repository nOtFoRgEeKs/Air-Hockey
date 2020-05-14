from abc import ABCMeta, abstractmethod
import pygame

from common import GameClock, GameUtils, GameConfig
from libs import Point, Vector2D


class BaseInput(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_position() -> Point:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_velocity() -> Vector2D:
        raise NotImplementedError

    enabled = False


class MouseInput(BaseInput):
    _MOUSE_POS: Point = Point()
    _MOUSE_VEL: Vector2D = Vector2D()

    @staticmethod
    def get_velocity() -> Vector2D:
        MouseInput._MOUSE_VEL.value = pygame.mouse.get_rel()
        MouseInput._MOUSE_VEL /= GameClock.get_time()
        return MouseInput._MOUSE_VEL

    @staticmethod
    def get_position() -> Point:
        MouseInput._MOUSE_POS.value = pygame.mouse.get_pos()
        return MouseInput._MOUSE_POS


class AIInput(BaseInput):
    _AI_POS: Point = Point()

    @staticmethod
    def get_velocity() -> Vector2D:
        # raise NotImplementedError
        return Vector2D()

    @staticmethod
    def get_position() -> Point:
        # raise NotImplementedError
        AIInput._AI_POS.value = GameUtils.inverted_point(pygame.mouse.get_pos(), GameConfig.FIELD_LOCATION,
                                                         GameConfig.FIELD_DIMENSION)
        return AIInput._AI_POS


class NetworkInput(BaseInput):
    @staticmethod
    def get_velocity() -> Vector2D:
        raise NotImplementedError

    @staticmethod
    def get_position() -> Point:
        raise NotImplementedError
