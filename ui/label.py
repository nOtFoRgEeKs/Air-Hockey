from typing import Union, Tuple, Optional

import pygame

from libs import Point


class Label(pygame.sprite.Sprite):
    def __init__(self, *groups, font: pygame.font.Font, text: str,
                 color: Union[pygame.Color, Tuple[int, int, int]], center: Point):
        super().__init__(*groups)

        self._font = font
        self._text = text
        self._color = color
        self._center = center
        self.image: Optional[pygame.Surface] = None
        self.rect: Optional[pygame.Rect] = None

        self._generate_img()

    @property
    def font(self) -> pygame.font.Font:
        return self._font

    @font.setter
    def font(self, new_font: pygame.font.Font):
        self._font = new_font
        self._generate_img()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str):
        self._text = new_text
        self._generate_img()

    @property
    def color(self) -> Union[pygame.Color, Tuple[int, int, int]]:
        return self._color

    @color.setter
    def color(self, new_color: Union[pygame.Color, Tuple[int, int, int]]):
        self._color = new_color
        self._generate_img()

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, new_center: Point):
        self._center = new_center
        self.rect.center = new_center.value

    def update(self, *args):
        pass

    def _generate_img(self):
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect()
        self.rect.center = self._center.value
