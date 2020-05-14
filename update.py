import pygame

from common import ObjectId, ObjectsLibrary


def update_game(*args, **kwargs):
    paddle_grp = ObjectsLibrary.get_object(ObjectId.PADDLE_GROUP)
    paddle_grp.update()

    puck_grp = ObjectsLibrary.get_object(ObjectId.PUCK_GROUP)
    puck_grp.update()

    # TODO
    # Game update logic
    print(pygame.mouse.get_pos())
