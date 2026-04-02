# quiz/game.py
score = 0
def check_answer(user, correct):
    return user.lower() == correct.lower()
from quiz.questions import get_questions

def run_game():
    global score
    for q in get_questions():
        answer = q["a"]  # имитация ответа
        if check_answer(answer, q["a"]):
            score += 1
    return score
