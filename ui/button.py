from abc import ABC, abstractmethod
from typing import Optional

import pygame

from libs import Point
from ui import EventHandler


class AbstractButton(ABC, pygame.sprite.Sprite):
    @abstractmethod
    def mouse_click(self):
        raise NotImplementedError

    @abstractmethod
    def mouse_enter(self):
        raise NotImplementedError

    @abstractmethod
    def mouse_leave(self):
        raise NotImplementedError


class Button(AbstractButton):

    def __init__(self, *groups, img: pygame.Surface,
                 focused_img: pygame.Surface, center: Point):
        super().__init__(*groups)
        self._focused = False

        #  img_table |
        # -----------|--------------
        #   Focused  |
        #            |

        self._img_table = {False: img,
                           True: focused_img}
        self.image: Optional[pygame.Surface] = None
        self.rect: Optional[pygame.Rect] = None
        self._center = center
        self.on_mouse_click = EventHandler()
        self.on_mouse_enter = EventHandler()
        self.on_mouse_leave = EventHandler()

        self._generate_img()

    def mouse_click(self):
        self.on_mouse_click()

    def mouse_enter(self):
        self._focused = True
        self._generate_img()
        self.on_mouse_enter()

    def mouse_leave(self):
        self._focused = False
        self._generate_img()
        self.on_mouse_leave()

    def _generate_img(self):
        self.image = self._img_table[self._focused]
        self.rect = self.image.get_rect()
        self.rect.center = self._center.value


class ToggleButton(AbstractButton):

    def __init__(self, *groups, default_img: pygame.Surface, default_focused_img: pygame.Surface,
                 toggled_img: pygame.Surface, toggled_focused_img: pygame.Surface, center: Point):
        super().__init__(*groups)
        self._toggled = False
        self._focused = False

        #  img_table |   Toggled
        # -----------|--------------
        #   Focused  |
        #            |

        self._img_table = {False: {False: default_img, True: toggled_img},
                           True: {False: default_focused_img, True: toggled_focused_img}}
        self.image: Optional[pygame.Surface] = None
        self.rect: Optional[pygame.Rect] = None
        self._center = center
        self.on_mouse_click = EventHandler()
        self.on_mouse_enter = EventHandler()
        self.on_mouse_leave = EventHandler()

        self._generate_img()

    def mouse_click(self):
        self._toggled = not self._toggled
        self._generate_img()
        self.on_mouse_click()

    def mouse_enter(self):
        self._focused = True
        self._generate_img()
        self.on_mouse_enter()

    def mouse_leave(self):
        self._focused = False
        self._generate_img()
        self.on_mouse_leave()

    def _generate_img(self):
        self.image = self._img_table[self._focused][self._toggled]
        self.rect = self.image.get_rect()
        self.rect.center = self._center.value
