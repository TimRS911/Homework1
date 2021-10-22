def generator(number):
    cur = 1
    for i in range(1, number + 1):
        cur *= i
        yield cur

n = 12
for ind, el in enumerate(generator(n)):
    print(f'#{ind} + 1 {el}')
