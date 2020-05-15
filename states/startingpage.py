from common import GameStateId
from states import BaseGameState, GamePlay


class StartingPage(BaseGameState):

    def __init__(self):
        super().__init__()

    def start(self, *args, **kwargs):
        GamePlay.CURRENT_STATE = GameStateId.START_PAGE

    def pause(self, *args, **kwargs):
        pass

    def resume(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def render(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass
