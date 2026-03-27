if __name__ == "__main__":
    phrases = input().split(";")
    lengths = [len(phrase.strip().split(" ")) for phrase in phrases]
    print(f"{phrases=}")
    print(f"{lengths=}")