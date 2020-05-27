from __future__ import annotations

from abc import ABCMeta, abstractmethod
from collections import deque
from typing import Dict, Optional

import pygame

from common import GameStateId


class GamePlay:
    ACTIVE_STATE: Optional[GameStateId] = None
    PAUSED_STATE_STACK = deque()
    STATE_POOL: Dict[GameStateId, AbstractGameState] = dict()


class AbstractGameState(metaclass=ABCMeta):

    def __init__(self):
        self._sprites_group = pygame.sprite.Group()

    @abstractmethod
    def start(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def pause(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def resume(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def render(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def stop(self, *args, **kwargs):
        raise NotImplementedError
