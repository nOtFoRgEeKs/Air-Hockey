from __future__ import annotations

from typing import Callable

import pygame


class EventHandler:
    def __init__(self):
        self._callbacks = list()

    def __call__(self, *args, **kwargs):
        for callback_ in self._callbacks:
            callback_(*args, **kwargs)

    def __iadd__(self, callback_: Callable[..., None]) -> EventHandler:
        if callable(callback_):
            if callback_ not in self._callbacks:
                self._callbacks.append(callback_)
                return self
        else:
            raise TypeError('Callable expected')

    def __isub__(self, callback_: Callable[..., None]):
        if callback_ in self._callbacks:
            self._callbacks.remove(callback_)
            return self


class UIManager:

    def __init__(self):
        self._elements_to_track = set()
        self._elements_in_focus = set()

        self._focused_elements_when_mousedown = None

    def add(self, ui_elements_group: pygame.sprite.Group):
        for ui_element in ui_elements_group:
            if hasattr(ui_element, 'mouse_enter') \
                    and hasattr(ui_element, 'mouse_leave') \
                    and hasattr(ui_element, 'mouse_click'):
                self._elements_to_track.add(ui_element)

    def clear(self):
        self._elements_to_track.clear()
        self._elements_in_focus.clear()

    def update(self, *args, **kwargs):

        _mouse_pos = pygame.mouse.get_pos()
        _current_focused_elements = set(
            [ui_element for ui_element in self._elements_to_track
             if ui_element.rect.collidepoint(_mouse_pos)])

        _focus_entered = _current_focused_elements - self._elements_in_focus
        _focus_left = self._elements_in_focus - _current_focused_elements

        self._elements_in_focus = _current_focused_elements

        events = kwargs['game_events']
        _click_started = next((True for event in events
                               if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1),
                              False)
        if _click_started:
            self._focused_elements_when_mousedown = _current_focused_elements

        _clicked = next((True for event in events if
                         event.type == pygame.MOUSEBUTTONUP
                         and event.button == 1
                         and self._focused_elements_when_mousedown == _current_focused_elements),
                        False)

        for ui_element in _focus_entered:
            ui_element.mouse_enter()

        for ui_element in _focus_left:
            ui_element.mouse_leave()

        if _clicked:
            self._focused_elements_when_mousedown = None
            for ui_element in _current_focused_elements:
                ui_element.mouse_click()
