def fib_gen(num=10000):
    n_minus_2 = 0
    n_minus_1 = 1
    for i in range(num):
        n = n_minus_2 + n_minus_1
        yield n
        n_minus_2 = n_minus_1
        n_minus_1 = n

if __name__ == '__main__':
    fibs = fib_gen()
    even_fibs = (n for n in fibs if n % 2 == 0)
    small_even_fibs = filter(lambda x: x < 4000000, even_fibs)
    total = sum(small_even_fibs)
    print(total)
