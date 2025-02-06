import random

def generate_math_problem(level):
    """Generate math problems based on difficulty level"""
    if level < 5:
        # Basic addition and subtraction
        a = random.randint(1, 10 * level)
        b = random.randint(1, 10 * level)
        if random.choice([True, False]):
            return f"{a} + {b} = ?", a + b
        else:
            return f"{a} - {b} = ?", a - b
    elif level < 10:
        # Multiplication
        a = random.randint(1, level)
        b = random.randint(1, level)
        return f"{a} × {b} = ?", a * b
    else:
        # Mixed operations
        a = random.randint(1, level)
        b = random.randint(1, level)
        c = random.randint(1, level)
        if random.choice([True, False]):
            return f"{a} × {b} + {c} = ?", a * b + c
        else:
            return f"{a} × {b} - {c} = ?", a * b - c

def check_answer(user_answer, correct_answer):
    """Check if user's answer is correct"""
    try:
        return int(user_answer) == correct_answer
    except ValueError:
        return False