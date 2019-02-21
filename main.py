import flask
import json
from app.snakes import get_snake

app = flask.Flask(__name__)


@app.route("/<snake_name>/")
def index(snake_name):
    return """
        Check the code for this snake on 
        <a href="https://github.com/battlesnakeio/training-snakes">
            Github
        </a>
    """


@app.route("/<snake_name>/start", methods=["GET", "POST"])
def start(snake_name):
    snake = get_snake(snake_name)

    return json.dumps({"name": snake.name(), "color": snake.color()})


@app.route("/<snake_name>/move", methods=["GET", "POST"])
def move(snake_name):
    snake = get_snake(snake_name)
    data = flask.request.json
    gamestate = snake.payload_to_game_state(data)
    move = snake.move(gamestate)
    if move is None:
        return json.dumps({"move": "up"})

    if type(move) is tuple:
        raise Exception("don't do this")

    return json.dumps({"move": move.direction()})


@app.route("/<snake_name>/end", methods=["GET", "POST"])
def end(snake_name):
    snake = get_snake(snake_name)
    data = flask.request.json
    snake.end()
    return json.dumps({})


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080, debug=True)
    except Exception as e:
        raise e
