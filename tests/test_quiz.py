from quiz.game import check_answer

def check_answer(user, correct):
    return user.strip().lower() == correct.strip().lower()

from quiz.game import run_game

def test_game():
    assert run_game() >= 0
