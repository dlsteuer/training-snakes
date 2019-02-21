from app.logic.base_distances import BaseDistances


class PathDistances(BaseDistances):
    def closest_to(self, start, goals, gamestate):
        paths = gamestate.best_paths_to(start, goals, allow_length_1=True)
        if len(paths) == 0:
            return

        closest_goal = paths[0][0]
        return closest_goal

    def directions_to(self, goal, gamestate):
        paths = gamestate.best_paths_to(gamestate.me.head, [goal], allow_length_1=True)
        if len(paths) == 0:
            return

        path = paths[0][2]
        move = path[1] - gamestate.me.head
        return [move]
