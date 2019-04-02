def fun(num):
    a, b = 0, 1
    yield a
    yield b
    count = 0
    while count<num:
        # print(count)
        a, b = b, a+b
        count += 1
        yield b


res = fun(10)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
