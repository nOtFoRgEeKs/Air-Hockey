from typing import Union

import pygame
from common import ObjectsLibrary, ObjectId, PlayerType
from inputmanager import BaseInput, MouseInput, AIInput, NetworkInput
from libs import Point, Vector2D


class Paddle(pygame.sprite.Sprite):
    def __init__(self, *groups, start_center_location: Point,
                 input_manager: Union[BaseInput, MouseInput, AIInput, NetworkInput],
                 paddle_bound: pygame.Rect, player_type: PlayerType):
        super().__init__(*groups)
        self.image: pygame.Surface = ObjectsLibrary.get_object(ObjectId.IMAGE_PADDLE)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = start_center_location.value
        self.radius: int = self.rect.centerx - self.rect.x

        self.velocity = Vector2D()

        self.input: BaseInput = input_manager
        self._bound: pygame.Rect = paddle_bound
        self.player_type = player_type

    @property
    def center(self) -> Point:
        return Point(self.rect.centerx, self.rect.centery)

    @center.setter
    def center(self, new_center: Point):
        self.rect.centerx, self.rect.centery = new_center.value

    def update(self, *args):
        if self.input.enabled:
            _pos = self.input.get_position()
            _vel = self.input.get_velocity()

            if _pos.x < self._bound.left + self.radius:
                _pos.x = self._bound.left + self.radius
                _vel.x = 0
            elif _pos.x > self._bound.right - self.radius:
                _pos.x = self._bound.right - self.radius
                _vel.x = 0

            if _pos.y < self._bound.top + self.radius:
                _pos.y = self._bound.top + self.radius
                _vel.y = 0
            elif _pos.y > self._bound.bottom - self.radius:
                _pos.y = self._bound.bottom - self.radius
                _vel.y = 0

            self.rect.centerx, self.rect.centery = _pos.value
            self.velocity.value = _vel.value

    def __str__(self) -> str:
        return self.player_type.name
