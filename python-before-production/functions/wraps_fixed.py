import functools

def log_call(original_function):
    @functools.wraps(original_function)
    def new_function(**kwargs):
        return original_function(**kwargs)
    return new_function

@log_call
def fetch_weather(city, units):
    "Fetch the weather for a city."
    ...
