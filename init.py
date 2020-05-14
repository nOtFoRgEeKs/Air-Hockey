import pygame

from assets import Paddle, Puck
from common import GameConfig, GameColor, ObjectsLibrary, GameConstants, ObjectId, PlayerType
from inputmanager import MouseInput, AIInput


def load_images():
    ObjectsLibrary.set_object(ObjectId.IMAGE_FIELD, pygame.image.load(GameConstants.IMAGE_FIELD))
    ObjectsLibrary.set_object(ObjectId.IMAGE_PADDLE, pygame.image.load(GameConstants.IMAGE_PADDLE))
    ObjectsLibrary.set_object(ObjectId.IMAGE_PUCK, pygame.image.load(GameConstants.IMAGE_PUCK))


def load_sounds():
    pass


def init_game():
    # Initialize pygame modules
    pygame.init()

    # Load all media assets
    load_images()
    load_sounds()

    # Create game window
    window = pygame.display.set_mode(GameConfig.WINDOW_DIMENSION.value, GameConfig.WINDOW_FLAG)
    ObjectsLibrary.set_object(ObjectId.WINDOW, window)
    window.fill(GameColor.GRAY_20)
    pygame.display.set_caption(GameConfig.WINDOW_CAPTION)

    # Create sprites
    paddle_user = Paddle(start_center_location=GameConfig.USER_PADDLE_CENTER, input_manager=MouseInput,
                         paddle_bound=GameConfig.USER_PADDLE_BOUND, player_type=PlayerType.USER)
    ObjectsLibrary.set_object(ObjectId.PADDLE_USER, paddle_user)
    paddle_opponent = Paddle(start_center_location=GameConfig.OPPONENT_PADDLE_CENTER, input_manager=AIInput,
                             paddle_bound=GameConfig.OPPONENT_PADDLE_BOUND, player_type=PlayerType.OPPONENT)
    ObjectsLibrary.set_object(ObjectId.PADDLE_OPPONENT, paddle_opponent)

    puck = Puck(start_center_location=GameConfig.PUCK_CENTER)
    ObjectsLibrary.set_object(ObjectId.PUCK, puck)

    # Create sprite groups
    paddle_grp = pygame.sprite.Group()
    paddle_grp.add(paddle_user)
    paddle_grp.add(paddle_opponent)
    ObjectsLibrary.set_object(ObjectId.PADDLE_GROUP, paddle_grp)

    puck_grp = pygame.sprite.Group()
    puck_grp.add(puck)
    ObjectsLibrary.set_object(ObjectId.PUCK_GROUP, puck_grp)

    # Enable inputs
    MouseInput.enabled = True
    # AIInput.enabled = True

    # TODO
    # Other init logic
