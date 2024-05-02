#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to
    meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
    """
    count = 0
    coins.sort(reverse=True)
    for i in range(len(coins)):
        if coins[i] <= total:
            count += total // coins[i]
            total = total % coins[i]
            if total != 0 and total < coins[len(coins) - 1]:
                count = -1
            makeChange(coins, total)
    return count
    """
