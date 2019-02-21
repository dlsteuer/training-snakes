from app.logic import (
    BadMoves,
    ChaseTail,
    Eat,
    Kill,
    PathDistances,
    IncreaseBoardControl,
)
from app.snakes.base_snake import BaseSnake
from app.utils.vector import up, down, left, right


class ControlFreak(
    BaseSnake, BadMoves, ChaseTail, Eat, Kill, PathDistances, IncreaseBoardControl
):
    DIFFICULTY = 10

    def is_hungry(self, gs):
        paths = gs.best_paths_to(gs.me.head, gs.food)
        if len(paths) == 0:
            return
        if len(paths) == 1:
            distance_to_closest_food = paths[0][1]
            return gs.me.health < distance_to_closest_food * 2

        distance_to_second_closest_food = paths[1][1]
        return gs.me.health < distance_to_second_closest_food * 2 + 5

    def move(self, gamestate):
        options = [
            (self.eat, "simple eat"),
            (self.possible_kill, "possible kill"),
            (self.increase_board_control, "control"),
            (self.chase_tail, "tail"),
            (lambda gs: up, "up"),
            (lambda gs: down, "down"),
            (lambda gs: left, "left"),
            (lambda gs: right, "right"),
        ]
        return self.get_best_move(gamestate, options)
