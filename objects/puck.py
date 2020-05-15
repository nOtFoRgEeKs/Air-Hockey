import math
from typing import List

import pygame

from assets import AssetManager
from common import GameConfig, GameClock, AssetId
from libs import Point, Vector2D
from objects import Paddle


class Puck(pygame.sprite.Sprite):
    def __init__(self, *groups, start_location: Point):
        super().__init__(*groups)
        self.image: pygame.Surface = AssetManager.get_asset(AssetId.IMAGE_PUCK)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = start_location.value
        self.radius: int = int(math.ceil(self.rect.width / 2))

        self.velocity = Vector2D(0.0, 0.0)

    @property
    def center(self) -> Point:
        return Point(self.rect.centerx, self.rect.centery)

    @center.setter
    def center(self, new_center: Point):
        self.rect.centerx, self.rect.centery = new_center.value

    def update(self, *args):
        paddle_grp: pygame.sprite.Group = args[0]

        collided_paddle_list: List[Paddle] = pygame.sprite.spritecollide(self, paddle_grp, False,
                                                                         pygame.sprite.collide_circle)

        for collided_paddle in collided_paddle_list:
            vector_puck_to_paddle = Vector2D(collided_paddle.center - self.center)
            vector_paddle_to_puck = -vector_puck_to_paddle

            parallel_vel_puck, perpendicular_vel_puck = self.velocity.decompose(vector_puck_to_paddle)
            parallel_vel_paddle: Vector2D = collided_paddle.velocity.decompose(vector_paddle_to_puck)[0]

            parallel_vel_puck = ((-parallel_vel_puck) * GameConfig.COLLISION_COEFFICIENT
                                 + parallel_vel_paddle * GameConfig.PADDLE_MASS / GameConfig.PUCK_MASS)
            self.velocity = parallel_vel_puck + perpendicular_vel_puck

            if self.velocity.len > GameConfig.PUCK_MAX_SPEED:
                self.velocity = self.velocity.normalized * GameConfig.PUCK_MAX_SPEED

            _offset = (self.radius + collided_paddle.radius
                       - vector_puck_to_paddle.len + GameConfig.PUCK_PADDLE_STICKING_OFFSET)
            _offset_vec = self.velocity.normalized * _offset
            self.rect.centerx += _offset_vec.x
            self.rect.centery += _offset_vec.y

        # Check for field bound and goal
        if self.rect.centerx <= GameConfig.PUCK_BOUND.left + self.radius:
            self.velocity.x = -self.velocity.x
            self.rect.centerx = GameConfig.PUCK_BOUND.left + self.radius
        elif self.rect.centerx >= GameConfig.PUCK_BOUND.right - self.radius:
            self.velocity.x = -self.velocity.x
            self.rect.centerx = GameConfig.PUCK_BOUND.right - self.radius

        if self.rect.centery <= GameConfig.PUCK_BOUND.top + self.radius:
            self.velocity.y = -self.velocity.y
            self.rect.centery = GameConfig.PUCK_BOUND.top + self.radius
            # if GameConfig.GOAL_X_RANGE[0] < self.rect.centerx < GameConfig.GOAL_X_RANGE[1]:
            #     print('Goal Player')
            # else:
            #     self.velocity.y = -self.velocity.y
        elif self.rect.centery >= GameConfig.PUCK_BOUND.bottom - self.radius:
            self.velocity.y = -self.velocity.y
            self.rect.centery = GameConfig.PUCK_BOUND.bottom - self.radius
            # if GameConfig.GOAL_X_RANGE[0] < self.rect.centerx < GameConfig.GOAL_X_RANGE[1]:
            #     print('Goal Opponent')
            # else:
            #     self.velocity.y = -self.velocity.y

        _displacement: Vector2D = self.velocity * GameClock.get_time()
        if _displacement.len < 0.5:
            self.velocity *= 0

        self.rect.centerx += math.ceil(_displacement.x)
        self.rect.centery += math.ceil(_displacement.y)

        if self.velocity.len > GameConfig.PUCK_MIN_SPEED:
            self.velocity *= GameConfig.FIELD_FRICTION
