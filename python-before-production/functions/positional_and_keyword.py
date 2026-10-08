def greet(greeting: str, /, name: str, *, excited: bool) -> str:
    message = f"{greeting}, {name}"
    return message.upper() if excited else message

print(greet("Hello", "Alice", excited=True))
print(greet("Hi", name="Bob", excited=False))
