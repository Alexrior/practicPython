def read_names(N):
    names = []
    for _ in range(N):
        name = input()
        if name.strip():
            names.append(name)
    return names


if __name__ == "__main__":
    N = int(input())
    names = read_names(N)
    uni = []
    for name in names:
        if not uni:
            uni.append(name)
            continue
        if len(name) not in [len(u) for u in uni]:
            uni.append(name)
    print(f"{names=}")
    print(f"{uni=}")