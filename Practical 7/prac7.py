from flask import Flask, render_template

app = Flask(__name__)

def knapsack_solver(capacity, weights, values, item_count):
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(item_count + 1)]

    for i in range(item_count + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp_table[i][w] = 0
            elif weights[i-1] <= w:
                dp_table[i][w] = max(values[i-1] + dp_table[i-1][w-weights[i-1]], dp_table[i-1][w])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    max_profit = dp_table[item_count][capacity]
    w = capacity
    chosen_items = []

    for i in range(item_count, 0, -1):
        if max_profit <= 0:
            break
        if max_profit == dp_table[i-1][w]:
            continue
        else:
            chosen_items.append(i)
            max_profit -= values[i-1]
            w -= weights[i-1]

    return dp_table, dp_table[item_count][capacity], chosen_items

@app.route('/')
def display_knapsack():
    values = [3, 4, 5, 6]
    weights = [2, 3, 4, 5]
    capacity = 5
    item_count = len(values)

    dp_table, max_value, selected_items = knapsack_solver(capacity, weights, values, item_count)

    return render_template('knapsack_result.html', dp_table=dp_table, capacity=capacity, item_count=item_count, max_value=max_value, selected_items=selected_items)

if __name__ == '__main__':
    app.run(debug=True)
