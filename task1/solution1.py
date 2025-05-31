import inspect
from functools import wraps


def strict(func: callable) -> callable:
    sig = inspect.signature(func)

    @wraps(func)
    def inner(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        for param_name, value in bound_args.arguments.items():
            if type(value) is not sig.parameters[param_name].annotation:
                raise TypeError
        return func(*args, **kwargs)

    return inner


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def foo_1(a: str, b: int, c: bool, d: float) -> int:
    return 0


@strict
def foo_2() -> int:
    return 0
