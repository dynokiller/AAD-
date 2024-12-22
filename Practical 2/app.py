from flask import Flask, request, render_template, jsonify
import time

app = Flask(__name__)

def sum_using_loop(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return total

def sum_using_equation(N):
    return N * (N + 1) // 2

def sum_using_recursion(N):
    if N == 0:
        return 0
    else:
        return N + sum_using_recursion(N-1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    N = int(request.form['number'])

    start_time = time.time()
    loop_sum = sum_using_loop(N)
    loop_time = time.time() - start_time

    start_time = time.time()
    equation_sum = sum_using_equation(N)
    equation_time = time.time() - start_time

    start_time = time.time()
    recursion_sum = sum_using_recursion(N)
    recursion_time = time.time() - start_time

    results = {
        "loop_sum": loop_sum,
        "loop_time": loop_time,
        "equation_sum": equation_sum,
        "equation_time": equation_time,
        "recursion_sum": recursion_sum,
        "recursion_time": recursion_time
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
