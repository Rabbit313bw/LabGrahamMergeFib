from random import uniform
SEED = 1337

def generate_random_data(num_points, a: float, b: float) -> list:
    A = []
    for i in range(num_points):
        A.append([uniform(a, b), uniform(a, b)])
    return A

if __name__ == "__main__":
    A = generate_random_data(10, 0.0, 9.9)
    print(A)
    with open("./data/random_data.txt", "w") as f:
        for a in A:
            print(*a, file=f)
