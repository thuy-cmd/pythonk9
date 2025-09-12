n = int(input("Nhập số lượng học sinh: "))
names = []
for i in range(n):
    name = input(f"Nhập tên của học sinh thứ {i + 1}: ")
    names.append(name)
print(names)
cnt = 0
for name in names:
    if (name == "Ngô Bảo Châu"):
        cnt += 1