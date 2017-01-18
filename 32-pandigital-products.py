from itertools import permutations

def pandigital_products():
    for p in permutations('123456789*='):
        equation = ''.join(p).replace('=','==')
        if equation.index('*') > equation.index('=='):
            continue
        try:
            ans = eval(equation)
            if ans:
                print(equation)
                number = int(equation.split('==')[-1])
                yield number
        except:
            continue

if __name__ == '__main__':
    g = pandigital_products()
    print(sum(set(g)))
