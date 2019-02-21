from app.utils.game_state import GameState
from app.utils.vector import up, down, left, right
from app.snakes.base_snake import BaseSnake


class Snake3(BaseSnake):
    DIFFICULTY = 3

    def move(self, gamestate: GameState):
        first_food = gamestate.food[0]
        print(first_food, self._directions_to(first_food, gamestate))
        return gamestate.first_empty_direction(
            gamestate.me.head, self._directions_to(first_food, gamestate), up
        )

    def _directions_to(self, goal, gamestate):
        to_travel = goal - gamestate.me.head
        horizontal = [left, right] if goal.x < gamestate.me.head.x else [right, left]
        vertical = [up, down] if goal.y < gamestate.me.head.y else [down, up]
        if to_travel.x > to_travel.y:
            return horizontal + vertical
        return vertical + horizontal

    def name(self):
        return "Training Snake 3"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self, details):
        pass
