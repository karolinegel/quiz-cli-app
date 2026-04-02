from quiz.game import check_answer

def test_answer():
    assert check_answer("4", "4")

from quiz.game import run_game

def test_game():
    assert run_game() >= 0
