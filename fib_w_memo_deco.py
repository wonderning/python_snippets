

# from functools import wraps

# def memo(func):
#     cache={}
#     @wraps(func)
#     def wrap(*args):
#         if args not in cache:
#             cache[args]=func(*args)
#         return cache[args]
#     return wrap

# @memo
# def fib(i):
#     if i<2: return 1
#     return fib(i-1)+fib(i-2)


# print(fib(100))


from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def cnk(n, k):
    if k == 0:
        return 1  # the order of `if` should not change!!!
    if n == 0:
        return 0
    return cnk(n - 1, k) + cnk(n - 1, k - 1)

print(cnk(50, 30))
