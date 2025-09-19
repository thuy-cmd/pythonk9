s = 'hsg8ngay21thang4nam2023'
a = ''

res = ''
sum = 0

for char in s:
    if char.isdigit():
        a += char
        res += char
    else:
        if res:
            sum += int(res)
            res = ''

if res:
    sum += int(res)
print(a)

b = "Khong"
for i in range(len(a) - 1, -1, -1):
    if a[i] in '05':
        b = a[:i+1]
        break
print(b)
print(sum)
