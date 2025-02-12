import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Жадібний алгоритм для видачі решти.
    
    Параметри:
    amount (int): Сума, яку потрібно видати.
    coins (list): Доступні номінали монет (за замовчуванням [50, 25, 10, 5, 2, 1]).
    
    Повертає:
    dict: Словник, де ключ - номінал монети, значення - кількість монет.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Алгоритм динамічного програмування для видачі решти з мінімальною кількістю монет.
    
    Параметри:
    amount (int): Сума, яку потрібно видати.
    coins (list): Доступні номінали монет (за замовчуванням [50, 25, 10, 5, 2, 1]).
    
    Повертає:
    dict: Словник, де ключ - номінал монети, значення - кількість монет.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

def compare_algorithms(amount):
    """
    Функція для порівняння жадібного алгоритму та алгоритму динамічного програмування.
    
    Параметри:
    amount (int): Сума, яку потрібно видати.
    """
    start_greedy = time.time()
    greedy_result = find_coins_greedy(amount)
    end_greedy = time.time()
    
    start_dp = time.time()
    dp_result = find_min_coins(amount)
    end_dp = time.time()
    
    print(f"Сума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {end_greedy - start_greedy:.6f} сек")
    print(f"Динамічне програмування: {dp_result}, Час виконання: {end_dp - start_dp:.6f} сек")
    print("-" * 50)
    
# Тестування
for test_amount in [113, 217, 999, 5000]:
    compare_algorithms(test_amount)