from typing import Callable, Union, Tuple
import pygame

from libs import Point, Dimension

GameClock = pygame.time.Clock()


class GameUtils:
    @staticmethod
    def game_loop(framerate: int = 30, required_framerate=10):
        def game_loop_decorator(func: Callable):
            def wrapper(*args, **kwargs):
                GameClock.tick(framerate)
                is_running: bool = True
                while is_running:
                    _delta_time = GameClock.tick(framerate)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            is_running = False
                    if _delta_time * required_framerate <= 1000:
                        func(*args, **kwargs)
                pygame.quit()
                exit()

            return wrapper

        return game_loop_decorator

    @staticmethod
    def async_delay(delay: int = 100):
        delay_counter: int = 0
        while delay_counter <= delay:
            delay_counter += 1
            pygame.time.delay(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    delay_counter = delay + 1
                    pygame.quit()
                    exit()

    @staticmethod
    def inverted_point(point: Union[Point, Tuple[int, int]], origin: Point, dimension: Dimension) -> Union[
                        Point, Tuple[int, int]]:
        if type(point) is tuple:
            _inverted_point_x = dimension.width - (point[0] - origin.x) + origin.x
            _inverted_point_y = dimension.height - (point[1] - origin.y) + origin.y
            return _inverted_point_x, _inverted_point_y
        else:
            _inverted_point = Point()
            _inverted_point.x = dimension.width - (point.x - origin.x) + origin.x
            _inverted_point.y = dimension.height - (point.y - origin.y) + origin.y
            return _inverted_point


class ObjectsLibrary:
    _objects_dict: dict = dict()

    @staticmethod
    def get_object(object_id):
        if object_id in ObjectsLibrary._objects_dict.keys():
            return ObjectsLibrary._objects_dict[object_id]

    @staticmethod
    def set_object(object_id, game_object):
        if object_id not in ObjectsLibrary._objects_dict.keys():
            ObjectsLibrary._objects_dict[object_id] = game_object

    @staticmethod
    def del_object(object_id):
        if object_id in ObjectsLibrary._objects_dict.keys():
            game_object = ObjectsLibrary._objects_dict[object_id]
            del ObjectsLibrary._objects_dict[object_id]
            del game_object
