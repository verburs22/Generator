#sarah verburg 07-01

def odd_nums():
    start = 1
    while True:
        yield start
        start = start + 2


def calculate_pi():
    odds = odd_nums()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx


approx_pi = calculate_pi()
for i in range(100000):
    print(next(approx_pi))

# for i in range(100):
#     print(next(odds))
