def make_palindrome(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    odd_chars = [ch for ch in counts if counts[ch] % 2 == 1]
    if len(odd_chars) > 1:
        return "Нельзя составить палиндром"

    left = []
    middle = ""

    for ch in sorted(counts):
        left.append(ch * (counts[ch] // 2))
        if counts[ch] % 2 == 1:
            middle = ch

    left_part = "".join(left)
    return left_part + middle + left_part[::-1]


word = input()
print(make_palindrome(word))