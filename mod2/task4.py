n = input()

ok = True
if n == "":
    ok = False
else:
    i = 0
    while i < len(n):
        if n[i] < '0' or n[i] > '9':
            ok = False
            break
        i += 1

if not ok:
    print("Неверный ввод")
else:
    num = int(n)
    if num <= 0:
        print("Неверный ввод")
    else:
        x = num
        b2 = ""
        while x > 0:
            b2 = str(x % 2) + b2
            x = x // 2

        x = num
        b8 = ""
        while x > 0:
            b8 = str(x % 8) + b8
            x = x // 8

        x = num
        b16 = ""
        digits = "0123456789ABCDEF"
        while x > 0:
            r = x % 16
            b16 = digits[r] + b16
            x = x // 16

        print(f"{b2}, {b8}, {b16}")