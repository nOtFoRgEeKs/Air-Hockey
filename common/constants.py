import os
from enum import Enum, auto

import pygame

from libs import Point, Dimension


class GameColor:
    TRANSPARENT = pygame.Color(255, 255, 255, 0)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)

    LIGHT_BLUE = (106, 159, 181)

    GRAY_10 = pygame.Color(230, 230, 230)
    GRAY_20 = pygame.Color(205, 205, 205)
    GRAY_30 = pygame.Color(180, 180, 180)
    GRAY_40 = pygame.Color(155, 155, 155)


class GameConfig:
    FRAMERATE = 120
    REQUIRED_FRAMERATE = 60

    WINDOW_DIMENSION = Dimension(455, 650)  # 450, 625
    WINDOW_FLAG = 0  # pygame.FULLSCREEN
    WINDOW_CAPTION = 'Air Hockey'

    FIELD_LOCATION = Point(10, 30)
    FIELD_BOUNDARY_WIDTH = 5
    FIELD_DIMENSION = Dimension(435, 610)
    MIDFIELD_OFFSET = 2
    PUCK_BOUND_OFFSET = 2

    FIELD_INNER_ORIGIN = FIELD_LOCATION + (FIELD_BOUNDARY_WIDTH, FIELD_BOUNDARY_WIDTH)
    FIELD_INNER_DIMENSION = FIELD_DIMENSION - 2 * FIELD_BOUNDARY_WIDTH

    USER_PADDLE_CENTER = FIELD_LOCATION + (217, 574)
    OPPONENT_PADDLE_CENTER = FIELD_LOCATION + (217, 35)
    PUCK_CENTER = FIELD_LOCATION + (217, 306)

    USER_PADDLE_BOUND = pygame.Rect(
        (FIELD_INNER_ORIGIN + (0, FIELD_INNER_DIMENSION.height // 2 + MIDFIELD_OFFSET)).value,
        (FIELD_INNER_DIMENSION.width, FIELD_INNER_DIMENSION.height // 2 - MIDFIELD_OFFSET))
    OPPONENT_PADDLE_BOUND = pygame.Rect(
        FIELD_INNER_ORIGIN.value,
        (FIELD_INNER_DIMENSION.width, FIELD_INNER_DIMENSION.height // 2 - MIDFIELD_OFFSET))

    PUCK_BOUND = pygame.Rect((FIELD_INNER_ORIGIN + PUCK_BOUND_OFFSET).value,
                             (FIELD_INNER_DIMENSION - 2 * PUCK_BOUND_OFFSET).value)
    GOAL_X_RANGE = (FIELD_LOCATION.x + 154, FIELD_LOCATION.x + 279)

    FIELD_FRICTION = 0.9998
    PUCK_MAX_SPEED = 1
    PUCK_MIN_SPEED = 0.1

    PUCK_PADDLE_STICKING_OFFSET = 2
    PADDLE_MASS = 150.0
    PUCK_MASS = 100.0
    COLLISION_COEFFICIENT = 0.8

    GAME_LOGO_SIZE = 65
    GAME_LOGO_TEXT = 'AIR HOCKEY'
    GAME_LOGO_COLOR = GameColor.RED
    GAME_LOGO_CENTER = Point(228, 100)

    MENU_DEFAULT_SIZE = 26
    MENU_FOCUSED_SIZE = 40
    MENU_COLOR = GameColor.GRAY_40


class GameConstants:
    FOLDER_ASSETS = 'assets'
    FOLDER_IMAGES = 'images'
    FOLDER_SOUNDS = 'sounds'
    FOLDER_FONTS = 'fonts'

    PATH_IMAGE_FIELD = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'field.png')
    PATH_IMAGE_PADDLE = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'paddle.png')
    PATH_IMAGE_PUCK = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'puck.png')

    PATH_FONT_LOGO = os.path.join(FOLDER_ASSETS, FOLDER_FONTS, 'FFF_Tusj.ttf')
    PATH_FONT_MENU = os.path.join(FOLDER_ASSETS, FOLDER_FONTS, 'Amatic-Bold.ttf')


class AssetId(Enum):
    IMAGE_FIELD = auto()
    IMAGE_PADDLE = auto()
    IMAGE_PUCK = auto()

    FONT_LOGO = auto()
    FONT_MENU_DEFAULT = auto()
    FONT_MENU_FOCUSED = auto()


class PlayerType(Enum):
    USER = auto()
    OPPONENT = auto()


class GameStateId(Enum):
    START_MENU = auto()
    IN_GAME = auto()
    PAUSE_PAGE = auto()
    WAITING_PLAYER = auto()
