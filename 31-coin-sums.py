def coin_change(left, coins, count):
    if left == 0:
        return count

    if not coins:
        return 0

    coin, *coins_left = coins
    return sum(coin_change(left-coin*i, coins_left, count+1)
               for i
               in range(0, left//coin))


if __name__ == '__main__':
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    total = 200
    ans = coin_change(total, coins, 0)
