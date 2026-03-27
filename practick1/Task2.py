if __name__ == "__main__":
    N = int(input())
    numbers = list(range(N, N**2))
    unsquare = [pow(n, 0.5) for n in numbers] 

    print(f"{numbers=}")
    print(f"{unsquare=}")