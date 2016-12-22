def multiples_of_3_and_5(num=1000):
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            yield i

if __name__ == '__main__':
    print(sum(multiples_of_3_and_5()))
