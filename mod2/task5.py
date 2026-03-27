s = input()

parts = []
cur = ""
i = 0
while i < len(s):
    if s[i] == '.':
        parts.append(cur)
        cur = ""
    else:
        cur += s[i]
    i += 1
parts.append(cur)

i = len(parts) - 1
while i >= 0:
    print(parts[i])
    i -= 1