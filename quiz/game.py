# quiz/game.py
score = 0
def check_answer(user, correct):
    return user.lower() == correct.lower()
from quiz.questions import get_questions

from quiz.utils import shuffle_questions

def run_game():
    global score
    questions = shuffle_questions(get_questions())
    for q in questions:
        answer = q["a"]
        if check_answer(answer, q["a"]):
            score += 1
    return score
