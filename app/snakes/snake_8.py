from app.snakes.base_snake import BaseSnake
from app.utils.vector import up, down, left, right
from app.logic import BadMoves, ChaseTail, Eat, Kill, OrthogonalDistances


class TailChaser(BaseSnake, BadMoves, ChaseTail, Eat, Kill, OrthogonalDistances):
    DIFFICULTY = 8

    def move(self, gamestate):
        options = [
            (self.eat, "simple eat"),
            (self.possible_kill, "possible kill"),
            (self.chase_tail, "tail"),
            (lambda gs: up, "up"),
            (lambda gs: down, "down"),
            (lambda gs: left, "left"),
            (lambda gs: right, "right"),
        ]

        for f, taunt in options:
            desired_move = f(gamestate)
            if not self.bad_move(desired_move, gamestate):
                return desired_move

        return down
