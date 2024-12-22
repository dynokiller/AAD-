from flask import Flask, render_template, request

app = Flask(__name__)


def fractional_knapsack(profits, weights, W):
    n = len(profits)
    items = [(profits[i], weights[i], profits[i] / weights[i]) for i in range(n)]
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_profit = 0.0
    fractions = [0] * n
    
    for i in range(n):
        if W == 0:
            break
        if items[i][1] <= W:
            W -= items[i][1]
            total_profit += items[i][0]
            fractions[i] = 1
        else:
            fractions[i] = W / items[i][1]
            total_profit += items[i][0] * fractions[i]
            W = 0
    
    return items, fractions, total_profit
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        profits = list(map(int, request.form.get('profits').split(',')))
        weights = list(map(int, request.form.get('weights').split(',')))
        W = int(request.form.get('capacity'))
        
        # Calculate knapsack result
        items, fractions, total_profit = fractional_knapsack(profits, weights, W)
        
        # Zip items and fractions together for use in the template
        items_with_fractions = list(zip(items, fractions))
        
        return render_template('index.html', items_with_fractions=items_with_fractions, total_profit=total_profit)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
