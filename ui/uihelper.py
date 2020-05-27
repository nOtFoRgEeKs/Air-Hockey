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

    _ELEMENTS_TO_TRACK = set()
    _ELEMENTS_IN_FOCUS = set()

    _FOCUSED_ELEMENTS_WHEN_MOUSEDOWN = None
    _IS_CLEAR = True

    @staticmethod
    def add(ui_elements_group: pygame.sprite.Group):
        for ui_element in ui_elements_group:
            if hasattr(ui_element, 'mouse_enter') \
                    and hasattr(ui_element, 'mouse_leave') \
                    and hasattr(ui_element, 'mouse_click'):
                UIManager._ELEMENTS_TO_TRACK.add(ui_element)
        UIManager._IS_CLEAR = False

    @staticmethod
    def clear():
        UIManager._ELEMENTS_TO_TRACK.clear()
        UIManager._ELEMENTS_IN_FOCUS.clear()
        UIManager._FOCUSED_ELEMENTS_WHEN_MOUSEDOWN = None
        UIManager._IS_CLEAR = True

    @staticmethod
    def update(*args):

        _mouse_pos = pygame.mouse.get_pos()
        _current_focused_elements = set(
            [ui_element for ui_element in UIManager._ELEMENTS_TO_TRACK
             if ui_element.rect.collidepoint(_mouse_pos)])

        _focus_entered = _current_focused_elements - UIManager._ELEMENTS_IN_FOCUS
        _focus_left = UIManager._ELEMENTS_IN_FOCUS - _current_focused_elements

        UIManager._ELEMENTS_IN_FOCUS = _current_focused_elements

        events = args[0]
        _click_started = next((True for event in events
                               if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1),
                              False)
        if _click_started:
            UIManager._FOCUSED_ELEMENTS_WHEN_MOUSEDOWN = _current_focused_elements

        _clicked = next((True for event in events if
                         event.type == pygame.MOUSEBUTTONUP
                         and event.button == 1
                         and UIManager._FOCUSED_ELEMENTS_WHEN_MOUSEDOWN == _current_focused_elements),
                        False)

        for ui_element in _focus_entered:
            ui_element.mouse_enter()
            if UIManager._IS_CLEAR:
                return

        for ui_element in _focus_left:
            ui_element.mouse_leave()
            if UIManager._IS_CLEAR:
                return

        if _clicked:
            UIManager._FOCUSED_ELEMENTS_WHEN_MOUSEDOWN = None
            for ui_element in _current_focused_elements:
                ui_element.mouse_click()
                if UIManager._IS_CLEAR:
                    return
