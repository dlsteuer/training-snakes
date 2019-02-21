from app.utils.vector import Vector, up, down, left, right, noop
from app.snakes.base_snake import BaseSnake


class Snake0(BaseSnake):
    DIFFICULTY = 0

    def move(self, gamestate):

        current_vector = gamestate.me.current_direction
        if current_vector != noop:
            return current_vector

        head = gamestate.me.head
        l_wall = Vector(0, head.y)
        r_wall = Vector(gamestate.board_width - 1, head.y)
        t_wall = Vector(head.x, 0)
        b_wall = Vector(head.x, gamestate.board_width - 1)
        farthest = head.farthest([l_wall, r_wall, t_wall, b_wall])
        return farthest

    def name(self):
        return "Training Snake 0"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self, **kwargs):
        pass
