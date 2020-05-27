import pygame

from assets import AssetManager
from common import GameConfig, PlayerType, AssetId, GameColor, GameStateId
from inputmanager import MouseInput, AIInput
from objects import Paddle, Puck
from states import AbstractGameState, GamePlay


class InGame(AbstractGameState):
    def __init__(self):
        super().__init__()

        self._paddle_user = Paddle(start_location=GameConfig.USER_PADDLE_CENTER,
                                   input_manager=MouseInput,
                                   paddle_bound=GameConfig.USER_PADDLE_BOUND,
                                   player_type=PlayerType.USER)

        self._paddle_opponent = Paddle(start_location=GameConfig.OPPONENT_PADDLE_CENTER,
                                       input_manager=AIInput,
                                       paddle_bound=GameConfig.OPPONENT_PADDLE_BOUND,
                                       player_type=PlayerType.OPPONENT)

        self._puck = Puck(start_location=GameConfig.PUCK_CENTER)

        self._paddle_grp = pygame.sprite.Group()
        self._paddle_grp.add(self._paddle_user)
        self._paddle_grp.add(self._paddle_opponent)

        self._puck_grp = pygame.sprite.Group()
        self._puck_grp.add(self._puck)

        self._field_image = AssetManager.get_asset(AssetId.IMAGE_FIELD)

    def start(self, *args, **kwargs):
        GamePlay.ACTIVE_STATE = GameStateId.IN_GAME

    def pause(self, *args, **kwargs):
        pass

    def resume(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self._paddle_grp.update()
        self._puck_grp.update(self._paddle_grp)

    def render(self, *args, **kwargs):
        window: pygame.Surface = kwargs.get('game_window')
        window.fill(GameColor.GRAY_20)
        window.blit(self._field_image, GameConfig.FIELD_LOCATION.value)

        self._paddle_grp.draw(window)
        self._puck_grp.draw(window)

    def stop(self, *args, **kwargs):
        pass
