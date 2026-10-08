import collections

def log_call(original_function):
    counter_dict = collections.defaultdict(collections.Counter)
    args_counter = collections.Counter()
    def new_function(*args, **kwargs):
        message_list = []
        for value in args:
            args_counter[value] += 1
            ntimes_called = args_counter[value]
            total = args_counter.total()
            message_list.append(f"{value!r} ({ntimes_called}/{total})")
        for key, value in kwargs.items():
            counter_dict[key][value] += 1
            ntimes_called = counter_dict[key][value]
            total = counter_dict[key].total()
            message_list.append(f"{key}={value!r} ({ntimes_called}/{total})")
        message = ", ".join(message_list)
        print(f"calling {original_function.__name__} with {message}")
        return original_function(*args, **kwargs)
    return new_function

@log_call
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
