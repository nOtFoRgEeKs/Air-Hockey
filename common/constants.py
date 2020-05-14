import os
from enum import Enum, auto
import pygame

from libs import Point, Dimension


class GameConfig:
    FRAMERATE = 100
    REQUIRED_FRAMERATE = 30

    WINDOW_DIMENSION = Dimension((450, 625))
    WINDOW_FLAG = 0  # pygame.FULLSCREEN
    WINDOW_CAPTION = 'Air Hockey'

    FIELD_LOCATION = Point(10, 10)
    FIELD_BOUNDARY_WIDTH = 5
    FIELD_DIMENSION = Dimension(435, 610)

    USER_PADDLE_CENTER = FIELD_LOCATION + Point(217, 574)
    OPPONENT_PADDLE_CENTER = FIELD_LOCATION + Point(217, 35)
    PUCK_CENTER = FIELD_LOCATION + Point(217, 306)

    USER_PADDLE_BOUND = pygame.Rect((FIELD_LOCATION + Point(35, 338)).value, (365, 238))
    OPPONENT_PADDLE_BOUND = pygame.Rect((FIELD_LOCATION + Point(35, 35)).value, (365, 238))

    FIELD_BOUND = pygame.Rect((FIELD_LOCATION + Point(25, 25)).value, (385, 561))  # pygame.Rect((FIELD_LOCATION + Point(24, 24)).value, (386, 562))
    GOAL_X_RANGE = (FIELD_LOCATION.x + 154, FIELD_LOCATION.x + 279)

    FIELD_FRICTION = 0.9998
    PUCK_MAX_SPEED = 1
    PUCK_MIN_SPEED = 0.1


class GameColor:
    TRANSPARENT = pygame.Color(255, 255, 255, 0)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)

    GRAY_10 = pygame.Color(230, 230, 230)
    GRAY_20 = pygame.Color(205, 205, 205)
    GRAY_30 = pygame.Color(180, 180, 180)
    GRAY_40 = pygame.Color(155, 155, 155)


class GameConstants:
    FOLDER_ASSETS = 'assets'
    FOLDER_IMAGES = 'images'
    FOLDER_SOUNDS = 'sounds'

    IMAGE_FIELD = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'field1.png')
    IMAGE_PADDLE = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'paddle.png')
    IMAGE_PUCK = os.path.join(FOLDER_ASSETS, FOLDER_IMAGES, 'puck.png')


class ObjectId(Enum):
    WINDOW = auto()

    PADDLE_USER = auto()
    PADDLE_OPPONENT = auto()
    PADDLE_GROUP = auto()
    PUCK = auto()
    PUCK_GROUP = auto()

    IMAGE_FIELD = auto()
    IMAGE_PADDLE = auto()
    IMAGE_PUCK = auto()


class PlayerType(Enum):
    USER = auto()
    OPPONENT = auto()
