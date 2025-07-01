#sarah verburg

def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

for i in range(21):
    print(next(fib)) #infinate generator of fibonacci numbers
