txt = input("Nhap chuoi: ")
print(txt)
res = ''
for char in txt:
    if (char.isdigit()):
        res += char

print(res)
print(''.join(sorted(res, reverse=True)))