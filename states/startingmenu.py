import pygame

from assets import AssetManager
from common import AssetId, GameConfig, GameColor, GameEvents
from states import AbstractGameState, GamePlay
from ui import Label, ToggleButton, Button


class StartingMenu(AbstractGameState):

    def __init__(self):
        super().__init__()

        self._labels_grp = pygame.sprite.Group()
        self._buttons_grp = pygame.sprite.Group()

    def start(self, *args, **kwargs):
        self._generate_screen()
        GamePlay.ACTIVE_STATE = self

    def pause(self, *args, **kwargs):
        GamePlay.PAUSED_STATE_STACK.append(self)

    def resume(self, *args, **kwargs):
        GamePlay.ACTIVE_STATE = self

    def update(self, *args, **kwargs):
        self._ui_manager.update(*args, **kwargs)

    def render(self, *args, **kwargs):
        window: pygame.Surface = kwargs.get('game_window')
        window.fill(GameColor.GRAY_20)
        self._labels_grp.draw(window)
        self._buttons_grp.draw(window)

        # s = pygame.Surface((455, 650))
        # s.set_alpha(128)
        # s.fill((0,0,200))
        # window.blit(s, (0,0))

    def stop(self, *args, **kwargs):
        self._ui_manager.clear()
        self._labels_grp.empty()
        self._buttons_grp.empty()

    def _generate_screen(self):
        # Creating game logo as colored text label
        game_logo = Label(self._labels_grp, text=GameConfig.GAME_LOGO_TEXT, color=GameConfig.GAME_LOGO_COLOR,
                          font=AssetManager.get_asset(AssetId.FONT_LOGO), center=GameConfig.GAME_LOGO_CENTER)

        # Creating start menu entries
        # Getting fonts for menu entries
        font_menu_default: pygame.font.Font = AssetManager.get_asset(AssetId.FONT_MENU_DEFAULT)
        font_menu_focused: pygame.font.Font = AssetManager.get_asset(AssetId.FONT_MENU_FOCUSED)

        # Entry: Single player match
        single_play_default = font_menu_default.render(GameConfig.START_MENU_OPTION_1_TEXT, True,
                                                       GameConfig.START_MENU_COLOR).convert_alpha()
        single_play_focused = font_menu_focused.render(GameConfig.START_MENU_OPTION_1_TEXT, True,
                                                       GameConfig.START_MENU_COLOR).convert_alpha()
        single_play_button = Button(self._buttons_grp, img=single_play_default,
                                    focused_img=single_play_focused,
                                    center=GameConfig.START_MENU_OPTION_1_CENTER)
        single_play_button.on_mouse_click += self._click_callback_single_match

        # Entry: Online match
        online_play_default = font_menu_default.render(GameConfig.START_MENU_OPTION_2_TEXT, True,
                                                       GameConfig.START_MENU_COLOR).convert_alpha()
        online_play_focused = font_menu_focused.render(GameConfig.START_MENU_OPTION_2_TEXT, True,
                                                       GameConfig.START_MENU_COLOR).convert_alpha()
        online_play_button = Button(self._buttons_grp, img=online_play_default,
                                    focused_img=online_play_focused,
                                    center=GameConfig.START_MENU_OPTION_2_CENTER)
        online_play_button.on_mouse_click += self._click_callback_online_match

        # Entry: Music configuration
        music_on_default = font_menu_default.render(GameConfig.START_MENU_OPTION_3_DEFAULT_TEXT, True,
                                                    GameConfig.START_MENU_COLOR).convert_alpha()
        music_on_focused = font_menu_focused.render(GameConfig.START_MENU_OPTION_3_DEFAULT_TEXT, True,
                                                    GameConfig.START_MENU_COLOR).convert_alpha()
        music_off_default = font_menu_default.render(GameConfig.START_MENU_OPTION_3_TOGGLED_TEXT, True,
                                                     GameConfig.START_MENU_COLOR).convert_alpha()
        music_off_focused = font_menu_focused.render(GameConfig.START_MENU_OPTION_3_TOGGLED_TEXT, True,
                                                     GameConfig.START_MENU_COLOR).convert_alpha()

        music_settings_button = ToggleButton(self._buttons_grp, default_img=music_on_default,
                                             default_focused_img=music_on_focused,
                                             toggled_img=music_off_default,
                                             toggled_focused_img=music_off_focused,
                                             center=GameConfig.START_MENU_OPTION_3_CENTER)

        music_settings_button.on_mouse_click += self._click_callback_music_settings

        # Entry: Quit game
        quit_game_default = font_menu_default.render(GameConfig.START_MENU_OPTION_4_TEXT, True,
                                                     GameConfig.START_MENU_COLOR).convert_alpha()
        quit_game_focused = font_menu_focused.render(GameConfig.START_MENU_OPTION_4_TEXT, True,
                                                     GameConfig.START_MENU_COLOR).convert_alpha()
        quit_game_button = Button(self._buttons_grp, img=quit_game_default,
                                  focused_img=quit_game_focused,
                                  center=GameConfig.START_MENU_OPTION_4_CENTER)
        quit_game_button.on_mouse_click += self._click_callback_quit_game

        # Adding ui elements to ui manager to track events
        self._ui_manager.add(self._labels_grp)
        self._ui_manager.add(self._buttons_grp)

    def _click_callback_single_match(self, *args, **kwargs):
        pass

    def _click_callback_online_match(self, *args, **kwargs):
        pass

    def _click_callback_music_settings(self, *args, **kwargs):
        pass

    def _click_callback_quit_game(self, *args, **kwargs):
        pygame.event.post(GameEvents.QUIT_GAME)
