def log_call(original_function):
    def new_function(**kwargs):
        kwargs_message = ", ".join(
            f"{key}={value!r}" for key, value in kwargs.items()
        )
        print(f"calling {original_function.__name__} with {kwargs_message}")
        return original_function(**kwargs)
    return new_function

def get_users(city):
    ...

@log_call
def fetch_weather(city, units):
    ...

@log_call
def send_notification(user_id, message):
    ...

fetch_weather(city="Berlin", units="Celsius")
