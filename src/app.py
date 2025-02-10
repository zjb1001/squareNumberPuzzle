from flask import Flask, render_template, request, redirect, session
from game_logic import generate_math_problem, check_answer
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET'])
def index():
    if 'score' not in session:
        session['score'] = 0
        session['level'] = 1
    
    if 'max_limit' not in session:
        session['max_limit'] = 100  # Default max_limit

    problem, answer = generate_math_problem(session['level'], session['max_limit'])
    session['current_answer'] = answer
    session['start_time'] = time.time()  # Record start time
    return render_template('index.html', 
                           problem=problem, 
                           score=session['score'], 
                           level=session['level'],
                           max_limit=session['max_limit'])

@app.route('/check', methods=['POST'])
def check():
    user_answer = request.form.get('answer', '')
    correct_answer = session.get('current_answer')
    elapsed_time = time.time() - session.get('start_time')
    
    if check_answer(user_answer, correct_answer):
        # Time-based scoring: faster answers get more points
        time_bonus = max(0, int(10 - elapsed_time))  # Up to 10 extra points
        session['score'] += 10 + time_bonus
        session['level'] += 1
        feedback = {"message": f"Correct! 🎉 You earned {10 + time_bonus} points."}
    else:
        session['score'] = max(0, session['score'] - 5)
        # Decrease level, but not below 1
        session['level'] = max(1, session['level'] - 1)
        feedback = {"message": f"The correct answer was {correct_answer}"}
    
    problem, answer = generate_math_problem(session['level'], session['max_limit'])
    session['current_answer'] = answer
    session['start_time'] = time.time()
    
    return render_template('index.html', 
                         problem=problem,
                         score=session['score'],
                         level=session['level'],
                         feedback=feedback['message'],
                         elapsed_time=round(elapsed_time, 2),
                         max_limit=session['max_limit'])

@app.route('/update_max_limit', methods=['POST'])
def update_max_limit():
    max_limit = int(request.form.get('max_limit', 100))
    session['max_limit'] = max_limit
    return "OK"

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)