from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Dict

from common import GameStateId


class GamePlay:
    CURRENT_STATE: GameStateId = None
    STATE_POOL: Dict[GameStateId, BaseGameState] = dict()


class BaseGameState(metaclass=ABCMeta):

    def __init__(self):
        self.is_running = False

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
