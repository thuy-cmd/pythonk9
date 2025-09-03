"""
Nhập sâu kí tự, đếm số kí tự số có trong chuỗi, tính tổng các số có trong chuỗi
"""
s = input("Nhập chuỗi: ")
cnt = 0
sum = 0
temp = ''

for char in s:
    if char.isdigit():
        cnt+=1
        temp += char
    else:
        if temp != '':
            sum += int(temp)
            temp = ''

if temp != '':
    sum += int(temp)

print(f"Chuỗi: {s} có {cnt} kí tự số")
print(f"Tổng các số có trong xâu {s} là: {sum}")