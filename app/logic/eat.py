from app.utils.game_state import GameState


class Eat(object):
    HUNGER_THRESHOLD = 30

    def is_hungry(self, gamestate: GameState):
        return gamestate.me.health < self.HUNGER_THRESHOLD

    def eat(self, gs: GameState):
        if self.is_hungry(gs):
            closest_food = self.closest_to(gs.me.head, gs.food, gs)
            if closest_food is None:
                return None

            for v in self.directions_to(closest_food, gs):
                if gs.is_safe(gs.me.head + v):
                    return v
            return None
