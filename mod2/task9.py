s = input()

res = ""
i = 0
while i < len(s):
    if s[i] != ' ' and s[i] != '-' and s[i] != '(' and s[i] != ')':
        res += s[i]
    i += 1

print(res)