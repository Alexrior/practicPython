s=input()
print(f"{bin(int(s))[2:]}, {oct(int(s))[2:]}, {hex(int(s))[2:].upper()}" if s.isdigit() and int(s)>0 else "Неверный ввод")