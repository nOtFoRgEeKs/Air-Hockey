import pygame

from assets import AssetManager
from common import GameStateId, AssetId, GameConfig, GameColor
from libs import Point
from states import AbstractGameState, GamePlay
from ui import Label, ToggleButton


class StartingMenu(AbstractGameState):

    def __init__(self):
        super().__init__()

        self._labels_grp = pygame.sprite.Group()
        self._buttons_grp = pygame.sprite.Group()

        self._generate_screen()

    def start(self, *args, **kwargs):
        GamePlay.CURRENT_STATE = GameStateId.START_MENU

    def pause(self, *args, **kwargs):
        pass

    def resume(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self._ui_manager.update(*args, **kwargs)

    def render(self, *args, **kwargs):
        window: pygame.Surface = kwargs.get('game_window')
        window.fill(GameColor.GRAY_20)
        self._labels_grp.draw(window)
        self._buttons_grp.draw(window)

    def stop(self, *args, **kwargs):
        pass

    def _generate_screen(self):
        _game_logo = Label(self._labels_grp, text=GameConfig.GAME_LOGO_TEXT, color=GameConfig.GAME_LOGO_COLOR,
                           font=AssetManager.get_asset(AssetId.FONT_LOGO), center=GameConfig.GAME_LOGO_CENTER)

        _font_menu_default: pygame.font.Font = AssetManager.get_asset(AssetId.FONT_MENU_DEFAULT)
        _font_menu_focused: pygame.font.Font = AssetManager.get_asset(AssetId.FONT_MENU_FOCUSED)

        _sound_on_default = _font_menu_default.render('Music:  on', True, (0, 0, 0)).convert_alpha()
        _sound_on_focused = _font_menu_focused.render('Music:  on', True, (0, 0, 0)).convert_alpha()
        _sound_off_default = _font_menu_default.render('Music: off', True, (0, 0, 0)).convert_alpha()
        _sound_off_focused = _font_menu_focused.render('Music: off', True, (0, 0, 0)).convert_alpha()

        _sound_button = ToggleButton(self._buttons_grp, default_img=_sound_on_default,
                                     default_focused_img=_sound_on_focused, toggled_img=_sound_off_default,
                                     toggled_focused_img=_sound_off_focused, center=Point(200, 400))

        _sound_button.on_mouse_enter += lambda: print('enter')
        _sound_button.on_mouse_leave += lambda: print('leave')
        _sound_button.on_mouse_click += lambda: print('click')

        self._ui_manager.add(self._labels_grp)
        self._ui_manager.add(self._buttons_grp)
