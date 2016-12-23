"Utilities to help solving problems."

def prime_factors(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            yield i
    if num > 1:
        yield num
