s = input()

zeros = 0
ones = 0

i = 0
while i < len(s):
    if s[i] == '0':
        zeros += 1
    elif s[i] == '1':
        ones += 1
    i += 1

if zeros == ones:
    print("yes")
else:
    print("no")