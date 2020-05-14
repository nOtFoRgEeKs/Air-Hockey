from common import GameUtils, GameConfig
from init import init_game
from update import update_game
from render import render_game


@GameUtils.game_loop(framerate=GameConfig.FRAMERATE, required_framerate=GameConfig.REQUIRED_FRAMERATE)
def air_hockey_game(*args, **kwargs):
    update_game(*args, **kwargs)
    render_game(*args, **kwargs)


if __name__ == '__main__':
    init_game()
    air_hockey_game()
