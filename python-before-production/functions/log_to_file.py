import sys

def log_call(file):
    def decorator(original_function):
        def new_function(**kwargs):
            print(f"calling {original_function.__name__}", file=file)
            return original_function(**kwargs)
        return new_function
    return decorator

@log_call(file=sys.stderr)
def fetch_weather(*, city, units):
    ...

fetch_weather(city="Berlin", units="Celsius")
