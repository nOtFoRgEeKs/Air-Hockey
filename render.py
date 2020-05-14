import pygame

from common import ObjectsLibrary, ObjectId, GameConfig


def render_game(*args, **kwargs):
    window = ObjectsLibrary.get_object(ObjectId.WINDOW)
    field_image = ObjectsLibrary.get_object(ObjectId.IMAGE_FIELD)
    window.blit(field_image, GameConfig.FIELD_LOCATION.value)

    paddle_grp = ObjectsLibrary.get_object(ObjectId.PADDLE_GROUP)
    puck_grp = ObjectsLibrary.get_object(ObjectId.PUCK_GROUP)
    paddle_grp.draw(window)
    puck_grp.draw(window)

    # TODO
    # Game render logic

    pygame.display.update()
