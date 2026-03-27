if __name__ == "__main__":
    prices = list(map(float, input().split(" ")))
    K = float(input())
    M = float(input())

    discount = [price - (price//K)*M for price in prices]
    print(f"{prices=}")
    print(f"{discount=}")