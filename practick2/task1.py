import re

date_pattern = re.compile(r"20\d{2}-[0,1]\d{1}-[0-3]\d{1} [1,2]\d{1}:[0-5]\d{1}:[0-5]\d{1}")

if __name__ == "__main__":
    print("Введите текст:")
    TEXT = input()
    dates = date_pattern.findall(TEXT)
    print(*dates, sep="\n")