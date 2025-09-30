import random

def generate_dense_sample():
    directions = ['U', 'D', 'L', 'R']
    print(1)  # number of test cases
    print(100, 100)  # matrix size
    for _ in range(100):
        row = [random.choice(directions) for _ in range(100)]
        print(' '.join(row))

generate_dense_sample()
