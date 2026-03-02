from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")

def simple_decorator(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {func.__name__} with arguments:")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Area of rectangle is {result}")
        return result
    return wrapper

@simple_decorator
def calculate_area(a: float, b: float) -> float:
    if (a < 0) or (b < 0):
        raise ValueError("a and b must be non-negative")
    return a * b

calculate_area(1, 10)
calculate_area(a=2, b=10)
calculate_area(3, b=10)

