from app.snakes.snake_11 import SurroundSnake
from app.snakes.snake_10 import ControlFreak
from app.snakes.snake_9 import TailChaser2
from app.snakes.snake_8 import TailChaser
from app.snakes.snake_7 import AttemptKillsSnake
from app.snakes.snake_6 import SimpleSometimesHungrySnake
from app.snakes.snake_5 import SimpleHungrySnake
from app.snakes.snake_4 import ScaredSnake
from app.snakes.snake_3 import Snake3
from app.snakes.snake_2 import Snake2
from app.snakes.snake_1 import Snake1
from app.snakes.snake_0 import Snake0

_snakes = None

SNAKE_CLASSES = [
    Snake0,
    Snake1,
    Snake2,
    Snake3,
    ScaredSnake,
    SimpleHungrySnake,
    SimpleSometimesHungrySnake,
    AttemptKillsSnake,
    TailChaser,
    TailChaser2,
    ControlFreak,
    SurroundSnake,
]


def get_snake(snake_name):
    global _snakes

    if _snakes is None:
        _snakes = {}
        for snake_class in SNAKE_CLASSES:
            snake = snake_class()
            name = "snake_%d" % snake.DIFFICULTY
            _snakes[name] = snake

    return _snakes.get(snake_name, Snake1())
