import random

def generate_math_problem(level, max_limit=20):
    base = random.randint(1, max(2, min(level, max_limit)))
    answer = base * base
    problem = f"what is {base} x {base} = ?"
    return problem, answer

def check_answer(user_answer, correct_answer):
    try:
        user_answer = int(user_answer.strip())
        return user_answer == correct_answer
    except (ValueError, AttributeError):
        return False