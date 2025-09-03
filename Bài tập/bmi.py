def bmi():
    chieuCao = float(input("Nhap chieu cao cua ban (m): "))
    canNang = float(input("Nhap can nang cua ban (kg): "))

    while (chieuCao <= 0 and canNang <= 0):
        print("Vui long nhap dung chieu cao hoac can nang cua ban (phai lon hon 0)")
        chieuCao = float(input("Nhap lai chieu cao cua ban (m): "))
        canNang = float(input("Nhap lai can nang cua ban (kg): "))
    else:
        while (chieuCao <= 0):
            chieuCao = float(input("Nhap lai chieu cao cua ban (m): "))
        while (canNang <= 0):
            canNang = float(input("Nhap lai can nang cua ban (kg): "))

    bmi = round(canNang/(chieuCao*chieuCao),2)

    print(f"Chieu cao cua ban la {chieuCao}m, can nang cua ban la {canNang}kg")
    print(f"Chi so BMI cua ban la: {bmi}")

    if bmi < 18.5: print("Gầy")
    elif bmi <= 22.9: print("Bình thường")
    elif bmi <= 24.9: print("Tiền béo phì")
    elif bmi <= 30: print("Béo phì độ 1")
    else: print("Béo phì độ 2")

bmi()
