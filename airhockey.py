import pygame

from assets import AssetManager
from common import GameConfig, GameUtils, AssetId, GameConstants, GameColor, GameStateId
from inputmanager import MouseInput
from libs import SingletonMeta
from states import GamePlay, BaseGameState, StartingPage, InGame


class AirHockeyGame(metaclass=SingletonMeta):
    def __init__(self):
        # Initialize pygame modules
        pygame.init()

        # Load all media assets
        AirHockeyGame._load_images()
        AirHockeyGame._load_sounds()

        # Create game window
        self._game_window: pygame.Surface = pygame.display.set_mode(GameConfig.WINDOW_DIMENSION.value,
                                                                    GameConfig.WINDOW_FLAG)
        pygame.display.set_caption(GameConfig.WINDOW_CAPTION)

        # Enable inputs
        MouseInput.enabled = True
        # AIInput.enabled = True

        # Initialize all the game states
        AirHockeyGame._initialize_game_states()

        # Set the starting game state
        GamePlay.STATE_POOL[GameStateId.IN_GAME].start()

        # TODO
        # Other init logic

    @GameUtils.game_loop(framerate=GameConfig.FRAMERATE, required_framerate=GameConfig.REQUIRED_FRAMERATE)
    def play_game(self):
        _game_state: BaseGameState = GamePlay.STATE_POOL[GamePlay.CURRENT_STATE]

        _game_state.update()

        self._game_window.fill(GameColor.GRAY_20)
        _game_state.render(game_window=self._game_window)
        pygame.display.update()

    def quit_game(self):
        pygame.quit()

    @staticmethod
    def _load_images():
        AssetManager.set_asset(AssetId.IMAGE_FIELD, pygame.image.load(GameConstants.PATH_IMAGE_FIELD))
        AssetManager.set_asset(AssetId.IMAGE_PADDLE, pygame.image.load(GameConstants.PATH_IMAGE_PADDLE))
        AssetManager.set_asset(AssetId.IMAGE_PUCK, pygame.image.load(GameConstants.PATH_IMAGE_PUCK))

    @staticmethod
    def _load_sounds():
        pass

    @staticmethod
    def _initialize_game_states():
        GamePlay.STATE_POOL[GameStateId.START_PAGE] = StartingPage()
        GamePlay.STATE_POOL[GameStateId.IN_GAME] = InGame()
