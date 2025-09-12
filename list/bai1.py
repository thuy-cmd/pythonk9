n = int(input("Nhập số người: "))
ages = []
for i in range(n):
    ages.append(int(input(f"Nhâp tuổi người thứ {i + 1}: ")))

print(ages)
print(ages[::-1])
sum = 0
cnt = 0
for age in ages:
    sum += age
    cnt += 1
print(f"Độ tuổi trung bình là: {sum / cnt}")