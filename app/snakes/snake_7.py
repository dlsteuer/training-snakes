import random
from app.snakes.base_snake import BaseSnake
from app.snakes.snake_6 import SimpleSometimesHungrySnake


class AttemptKillsSnake(BaseSnake):
    DIFFICULTY = 7
    HUNGER_THRESHOLD = 30

    def move(self, gamestate):

        if len(gamestate.possible_kill_coords) > 0:
            goal = random.choice(gamestate.possible_kill_coords)
            return goal - gamestate.me.head

        return SimpleSometimesHungrySnake().move(gamestate)

    def name(self):
        return "Training Snake 7"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
