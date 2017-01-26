from itertools import chain

def threes_and_fives_gen(num=1000):
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            yield i

def threes_and_fives_fun(n):
    return set(chain(range(3, n+1, 3), range(5, n+1, 5)))

def solve(n):
    return sum(
        filter(lambda x: x%3==0 or x%5==0,
               range(1, n)
        )
    )

if __name__ == '__main__':
    print(sum(three_and_fives_gen(10000000)))
