import pygame

from assets import AssetManager
from common import GameConfig, GameUtils, AssetId, GameConstants, GameStateId
from inputmanager import MouseInput
from libs import SingletonMeta
from states import GamePlay, AbstractGameState, StartingMenu, InGame


class AirHockeyGame(metaclass=SingletonMeta):
    def __init__(self):
        # Initialize pygame modules
        pygame.init()

        # Create game window
        self._game_window: pygame.Surface = pygame.display.set_mode(GameConfig.WINDOW_DIMENSION.value,
                                                                    GameConfig.WINDOW_FLAG)
        pygame.display.set_caption(GameConfig.WINDOW_CAPTION)

        # Load all media assets
        AirHockeyGame._load_images()
        AirHockeyGame._load_sounds()
        AirHockeyGame._load_fonts()

        # Enable inputs
        MouseInput.enabled = True
        # AIInput.enabled = True

        # Initialize all the game states
        AirHockeyGame._initialize_game_states()

        # Set the starting game state
        GamePlay.STATE_POOL[GameStateId.START_MENU].start()

        # TODO
        # Other init logic

    @GameUtils.game_loop(framerate=GameConfig.FRAMERATE, required_framerate=GameConfig.REQUIRED_FRAMERATE)
    def play_game(self, *args, **kwargs):
        kwargs['game_window'] = self._game_window
        _game_state: AbstractGameState = GamePlay.STATE_POOL[GamePlay.CURRENT_STATE]

        _game_state.update(*args, **kwargs)
        _game_state.render(*args, **kwargs)

        pygame.display.update()

    def quit_game(self):
        pygame.quit()

    @staticmethod
    def _load_images():
        AssetManager.set_asset(AssetId.IMAGE_FIELD, pygame.image.load(GameConstants.PATH_IMAGE_FIELD).convert_alpha())
        AssetManager.set_asset(AssetId.IMAGE_PADDLE, pygame.image.load(GameConstants.PATH_IMAGE_PADDLE).convert_alpha())
        AssetManager.set_asset(AssetId.IMAGE_PUCK, pygame.image.load(GameConstants.PATH_IMAGE_PUCK).convert_alpha())

    @staticmethod
    def _load_sounds():
        pass

    @staticmethod
    def _load_fonts():
        AssetManager.set_asset(AssetId.FONT_LOGO,
                               pygame.font.Font(GameConstants.PATH_FONT_LOGO, GameConfig.GAME_LOGO_SIZE))
        AssetManager.set_asset(AssetId.FONT_MENU_DEFAULT,
                               pygame.font.Font(GameConstants.PATH_FONT_MENU, GameConfig.MENU_DEFAULT_SIZE))
        AssetManager.set_asset(AssetId.FONT_MENU_FOCUSED,
                               pygame.font.Font(GameConstants.PATH_FONT_MENU, GameConfig.MENU_FOCUSED_SIZE))

    @staticmethod
    def _initialize_game_states():
        GamePlay.STATE_POOL[GameStateId.START_MENU] = StartingMenu()
        GamePlay.STATE_POOL[GameStateId.IN_GAME] = InGame()
