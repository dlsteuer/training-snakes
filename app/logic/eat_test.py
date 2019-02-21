from app.utils.test import build_test_gamestate
from app.logic import Eat, PathDistances
from app.snakes.base_snake import BaseSnake


def test_eat_closest():
    class EatingSnake(BaseSnake, Eat, PathDistances):
        def move(self, gamestate):
            return self.eat(gs)

    gs = build_test_gamestate(
        3, 3, me=[(0, 1), (0, 2)], food=[(0, 0), (1, 2)], health=29
    )
    move = EatingSnake().move(gs)
    assert move.direction() == "up"
