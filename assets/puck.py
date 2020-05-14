import math
from typing import List

import pygame

from assets import Paddle
from common import ObjectsLibrary, ObjectId, GameConfig, GameClock
from libs import Point, Vector2D


class Puck(pygame.sprite.Sprite):
    def __init__(self, *groups, start_center_location: Point):
        super().__init__(*groups)
        self.image: pygame.Surface = ObjectsLibrary.get_object(ObjectId.IMAGE_PUCK)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = start_center_location.value
        self.radius: int = int(math.ceil(self.rect.width / 2))

        self.velocity = Vector2D(0.0, 0.0)

    @property
    def center(self) -> Point:
        return Point(self.rect.centerx, self.rect.centery)

    @center.setter
    def center(self, new_center: Point):
        self.rect.centerx, self.rect.centery = new_center.value

    def update(self, *args):

        paddle_grp: pygame.sprite.Group = ObjectsLibrary.get_object(ObjectId.PADDLE_GROUP)

        collided_paddle_list: List[Paddle] = pygame.sprite.spritecollide(self, paddle_grp, False,
                                                                         pygame.sprite.collide_circle)

        for collided_paddle in collided_paddle_list:
            vector_puck_to_paddle = Vector2D(collided_paddle.center - self.center)
            vector_paddle_to_puck = -vector_puck_to_paddle

            parallel_vel_puck, perpendicular_vel_puck = self.velocity.decompose(vector_puck_to_paddle)
            parallel_vel_paddle: Vector2D = collided_paddle.velocity.decompose(vector_paddle_to_puck)[0]

            parallel_vel_puck = (-parallel_vel_puck) * 0.8 + parallel_vel_paddle * 1.5
            self.velocity = parallel_vel_puck + perpendicular_vel_puck

            if self.velocity.len > GameConfig.PUCK_MAX_SPEED:
                self.velocity = self.velocity.normalized * GameConfig.PUCK_MAX_SPEED

            _offset = self.radius + collided_paddle.radius - vector_puck_to_paddle.len + 2
            _offset_vec = self.velocity.normalized * _offset
            self.rect.centerx += _offset_vec.x
            self.rect.centery += _offset_vec.y

        # Check for field bound and goal
        if self.rect.centerx <= GameConfig.FIELD_BOUND.left:
            self.velocity.x = -self.velocity.x
            self.rect.centerx = GameConfig.FIELD_BOUND.left
        elif self.rect.centerx >= GameConfig.FIELD_BOUND.right:
            self.velocity.x = -self.velocity.x
            self.rect.centerx = GameConfig.FIELD_BOUND.right

        if self.rect.centery <= GameConfig.FIELD_BOUND.top:
            self.velocity.y = -self.velocity.y
            self.rect.centery = GameConfig.FIELD_BOUND.top
            # if GameConfig.GOAL_X_RANGE[0] < self.rect.centerx < GameConfig.GOAL_X_RANGE[1]:
            #     print('Goal Player')
            # else:
            #     self.velocity.y = -self.velocity.y
        elif self.rect.centery >= GameConfig.FIELD_BOUND.bottom:
            self.velocity.y = -self.velocity.y
            self.rect.centery = GameConfig.FIELD_BOUND.bottom
            # if GameConfig.GOAL_X_RANGE[0] < self.rect.centerx < GameConfig.GOAL_X_RANGE[1]:
            #     print('Goal Opponent')
            # else:
            #     self.velocity.y = -self.velocity.y

        print(self.velocity.len)

        _displacement: Vector2D = self.velocity * GameClock.get_time()
        if _displacement.len < 0.5:
            self.velocity *= 0

        self.rect.centerx += math.ceil(_displacement.x)
        self.rect.centery += math.ceil(_displacement.y)

        if self.velocity.len > GameConfig.PUCK_MIN_SPEED:
            self.velocity *= GameConfig.FIELD_FRICTION
