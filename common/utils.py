from typing import Callable, Union, Tuple

import pygame

from libs import Point, Dimension

GameClock = pygame.time.Clock()


class GameUtils:
    @staticmethod
    def game_loop(framerate: int, required_framerate: int):
        def game_loop_decorator(func: Callable[..., None]):
            def wrapper(*args, **kwargs):
                while True:
                    _delta_time = GameClock.tick(framerate)
                    _game_events = pygame.event.get()
                    kwargs['game_events'] = _game_events
                    if next((True for event in _game_events if event.type == pygame.QUIT), False):
                        break
                    if _delta_time * required_framerate <= 1000:
                        func(*args, **kwargs)

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
    def inverted_point(point: Union[Point, Tuple[int, int]],
                       origin: Point, dimension: Dimension) -> Union[Point, Tuple[int, int]]:
        if type(point) is tuple:
            _inverted_point_x = dimension.width - (point[0] - origin.x) + origin.x
            _inverted_point_y = dimension.height - (point[1] - origin.y) + origin.y
            return _inverted_point_x, _inverted_point_y
        else:
            _inverted_point = Point()
            _inverted_point.x = dimension.width - (point.x - origin.x) + origin.x
            _inverted_point.y = dimension.height - (point.y - origin.y) + origin.y
            return _inverted_point
