from flask import Flask, render_template_string, request
import time
from collections import Counter

app = Flask(__name__)

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    coin_used = [-1] * (amount + 1)
    dp[0] = 0 
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1, {}
    
    result_coins = []
    while amount > 0:
        result_coins.append(coin_used[amount])
        amount -= coin_used[amount]
    
    coin_count = dict(Counter(result_coins))
    
    return dp[amount + sum(result_coins)], coin_count

@app.route('/', methods=['GET', 'POST'])
def coin_change():
    result = None
    coins_used = {}
    execution_time = None
    
    if request.method == 'POST':
        coins = [int(x) for x in request.form.get('coins').split(',')]
        amount = int(request.form.get('amount'))
        
        start_time = time.time()
        result, coins_used = min_coins(coins, amount)
        execution_time = time.time() - start_time

    html_content = '''
    <html>
    <head>
        <title>Coin Change Problem</title>
    </head>
    <body>
        <h1>Coin Change Problem</h1>
        <form method="POST">
            <label for="coins">Enter the coin denominations (comma separated):</label><br>
            <input type="text" id="coins" name="coins" required><br><br>
            <label for="amount">Enter the amount:</label><br>
            <input type="number" id="amount" name="amount" required><br><br>
            <button type="submit">Calculate Minimum Coins</button>
        </form>

        {% if result is not none %}
            <h2>Results:</h2>
            {% if result == -1 %}
                <p>It's impossible to make the amount with the given coins.</p>
            {% else %}
                <p>Minimum number of coins required: {{ result }}</p>
                <h3>Coins Used:</h3>
                <ul>
                {% for coin, count in coins_used.items() %}
                    <li>Coin: {{ coin }}, Count: {{ count }}</li>
                {% endfor %}
                </ul>
                <p>Execution time: {{ execution_time }} seconds</p>
            {% endif %}
        {% endif %}
    </body>
    </html>
    '''
    
    return render_template_string(html_content, result=result, coins_used=coins_used, execution_time=execution_time)

app.run(debug=True)
