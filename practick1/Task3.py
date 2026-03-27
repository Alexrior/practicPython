if __name__ == "__main__":
    numbers = list(map(int, input().split(" ")))
    K = int(input())
    
    divisibles = [n for n in numbers if n%K == 0]

    print(f"{numbers=}")
    print(f"{divisibles=}")