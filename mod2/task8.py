s = input()

word = ""
res = ""
i = 0

while i < len(s):
    if s[i] == ' ':
        if word != "":
            res += word[len(word) - 1]
            word = ""
    else:
        word += s[i]
    i += 1

if word != "":
    res += word[len(word) - 1]

print(res)