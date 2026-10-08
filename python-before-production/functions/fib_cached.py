from log_call import log_call

def cache(func):
    results = {}
    def wrapper(n):
        if n not in results:
            results[n] = func(n)
        return results[n]
    return wrapper

@cache
@log_call
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
