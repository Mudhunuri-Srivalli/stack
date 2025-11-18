class rangeIterator():
    def __init__(self,start_value,end_value):
      self.curr_value=start_value
      self.limit=
    def __iter__(self):
       return self
    def __next__(self):




 from typing import Iterator

def fib_infinite() -> Iterator[int]:
    """
    Infinite Fibonacci generator:
    yields 0, 1, 1, 2, 3, 5, 8, ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b





from typing import Iterator, Optional

def range_like(start: int, stop: Optional[int] = None, step: int = 1) -> Iterator[int]:
    """
    Generator that behaves like built-in range():
    - range_like(stop) -> 0 .. stop-1
    - range_like(start, stop) -> start .. stop-1
    - accepts negative step
    """
    if stop is None:
        # called with one argument: range_like(stop)
        stop = start
        start = 0

    if step == 0:
        raise ValueError("range_like() step must not be zero")

    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step

       