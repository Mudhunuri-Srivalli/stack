
# Range-like Generator in Python


def my_range(start, stop=None, step=1):
    """
    Custom range generator that mimics Python's built-in range().
    
    Usage:
        my_range(stop)
        my_range(start, stop)
        my_range(start, stop, step)
    """
    if stop is None:
        stop = start
        start = 0
    
    if step == 0:
        raise ValueError("step cannot be zero")
    
    if step > 0:
        current = start
        while current < stop:
            yield current
            current += step
    else:
        current = start
        while current > stop:
            yield current
            current += step  



# Infinite Fibonacci Generator


def infinite_fibonacci():
    """
    A generator that yields Fibonacci numbers forever.
    Example: 0, 1, 1, 2, 3, 5, 8 ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



# Testing the Generators


print("Custom Range-like Generator Output:")
for num in my_range(2, 15, 3):
    print(num, end=" ")

print("\n\nFirst 10 Numbers of Infinite Fibonacci Generator:")
fibo_gen = infinite_fibonacci()

for _ in range(10):  
    print(next(fibo_gen), end=" ")
