from __future__ import annotations

from typing import Callable

import pygame


class EventHandler:
    def __init__(self):
        self._handlers = list()

    def __call__(self, *args, **kwargs):
        for _handler in self._handlers:
            _handler(*args, **kwargs)

    def __iadd__(self, _handler: Callable[..., None]) -> EventHandler:
        if callable(_handler):
            if _handler not in self._handlers:
                self._handlers.append(_handler)
                return self
        else:
            raise TypeError('Callable expected')

    def __isub__(self, _handler: Callable[..., None]):
        if _handler in self._handlers:
            self._handlers.remove(_handler)
            return self


class UIManager:

    def __init__(self):
        self._elements_to_track = set()
        self._elements_in_focus = set()

    def add(self, ui_elements_group: pygame.sprite.Group):
        for ui_element in ui_elements_group:
            if hasattr(ui_element, 'mouse_enter') \
                    and hasattr(ui_element, 'mouse_leave') \
                    and hasattr(ui_element, 'mouse_click'):
                self._elements_to_track.add(ui_element)

    def update(self, *args, **kwargs):

        _mouse_pos = pygame.mouse.get_pos()
        _current_focused_elements = set(
            [ui_element for ui_element in self._elements_to_track
             if ui_element.rect.collidepoint(_mouse_pos)])

        _focus_entered = _current_focused_elements - self._elements_in_focus
        _focus_left = self._elements_in_focus - _current_focused_elements

        self._elements_in_focus = _current_focused_elements

        events = kwargs['game_events']
        _clicked = next((True for event in events
                         if event.type == pygame.MOUSEBUTTONUP and event.button == 1),
                        False)

        for ui_element in _focus_entered:
            ui_element.mouse_enter()

        for ui_element in _focus_left:
            ui_element.mouse_leave()

        if _clicked:
            for ui_element in _current_focused_elements:
                ui_element.mouse_click()
