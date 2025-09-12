s = "TinHocTre2023"
lower = 0
upper = 0
cnt = 0

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        cnt += 1

n = len(s)
print(n)
min_l = n + 1
result = "KHONG CO"

for i in range(0, n):
    print(f"Lan {i}")
    isUpper = isLower = isDigit = 0
    for j in range(i, n):
        if (s[j].isupper()):
            print(j)
            print(s[j])
            isUpper = True
            print(f"Chu hoa {isUpper}")
        elif (s[j].islower()):
            print(j)
            print(s[j])
            isLower = True
            print(f"Chu thuong {isLower}")
        elif (s[j].isdigit()):
            print(j)
            print(s[j])
            isDigit = True
        if (isUpper and isLower and isDigit):
            lenght = j - i + 1
            print(lenght)
            if (lenght < min_l):
                min_l = lenght
                print(min_l)
                result = s[i:j+1]
                print(result)
                break

print(f"Sau {s} co: {upper} hoa, {lower} thuong, {cnt} so")
print(result)