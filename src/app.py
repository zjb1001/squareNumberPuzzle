from flask import Flask, render_template, request, redirect, session
import random
from game_logic import generate_math_problem, check_answer

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
        session['level'] = 1
    problem, answer = generate_math_problem(session['level'])
    session['current_answer'] = answer
    return render_template('index.html', problem=problem, score=session['score'], level=session['level'])

@app.route('/check', methods=['POST'])
def check():
    user_answer = request.form.get('answer', '').strip()
    if user_answer.isdigit() and int(user_answer) == session['current_answer']:
        session['score'] += 10
        session['level'] += 1
        feedback = "Correct! ��"
    else:
        feedback = f"Oops! The correct answer was {session['current_answer']}. Try again!"
        session['score'] = max(0, session['score'] - 5)
    
    return render_template('index.html', 
                         problem=generate_math_problem(session['level'])[0],
                         score=session['score'],
                         level=session['level'],
                         feedback=feedback)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)