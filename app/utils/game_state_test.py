from app.utils.test import build_test_gamestate
from app.utils.vector import Vector as V


def test_travel_times():
    gs = build_test_gamestate()
    travel_times = gs.travel_times(V(1, 1))
    assert travel_times == {
        "1_1": 0,
        "1_0": 1,
        "1_2": 1,
        "0_1": 1,
        "2_1": 1,
        "2_0": 2,
        "0_2": 2,
        "2_2": 2,
    }


def test_is_empty():
    gs = build_test_gamestate()
    assert gs.is_empty(V(0, 0)) is False  # snake is here
    assert gs.is_empty(V(0, 1)) is True


def test_empty_squares():
    gs = build_test_gamestate()
    es = gs.empty_squares()
    assert es == {
        "0_1": True,
        "0_2": True,
        "1_0": True,
        "1_1": True,
        "1_2": True,
        "2_0": True,
        "2_1": True,
        "2_2": True,
    }


def test_best_paths_to():
    gs = build_test_gamestate()
    paths = gs.best_paths_to(gs.me.head, [V(2, 2)])
    assert paths == [(V(2, 2), 5, [V(0, 0), V(1, 0), V(2, 0), V(2, 1), V(2, 2)])]


def test_empty():
    gs = build_test_gamestate(1, 2, me=[(0, 1), (0, 0)])
    assert gs.is_empty(V(0, 0)) is False
    assert gs.is_empty(V(0, 1)) is False


def test_distance_to():
    gs1 = build_test_gamestate(1, 3)
    dists1 = gs1.best_paths_to(V(0, 0), [V(0, 2)])
    expected1 = [(V(0, 2), 3, [V(0, 0), V(0, 1), V(0, 2)])]
    assert dists1 == expected1


def test_distance_to_multiple():
    gs = build_test_gamestate(1, 3)
    dists = gs.best_paths_to(V(0, 0), [V(0, 2), V(0, 1)], True)
    assert dists == [
        (V(0, 1), 2, [V(0, 0), V(0, 1)]),
        (V(0, 2), 3, [V(0, 0), V(0, 1), V(0, 2)]),
    ]


def test_safe_tails():
    gs = build_test_gamestate(
        1,
        2,
        me=[(0, 1), (0, 0), (0, 0)],
        opponents=[[(2, 1), (2, 0)], [(3, 1), (3, 0), (3, 0)]],
    )
    assert gs.safe_tails == [V(2, 0)]


def test_distance_to_turn_around():
    head = (2, 1)
    headV = V(2, 1)
    tail = (2, 0)
    tailV = V(2, 0)
    gs1 = build_test_gamestate(3, 3, [head, tail])
    dists1 = gs1.best_paths_to(headV, [tailV])
    expected1 = [(tailV, 4, [headV, V(1, 1), V(1, 0), tailV])]
    assert dists1 == expected1
