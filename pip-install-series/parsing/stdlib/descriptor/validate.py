class ge:
    _name: str

    def __init__(self, minimum: int) -> None:
        self.minimum = minimum

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = f"_{name}"

    def __get__(self, instance: object, owner: type) -> int:
        return getattr(instance, self._name)

    def __set__(self, instance: object, value: int) -> None:
        if value < self.minimum:
            raise ValueError(f"{value} below minimum {self.minimum}")
        setattr(instance, self._name, value)
