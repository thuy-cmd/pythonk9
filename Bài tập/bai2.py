s = "TinHocTre2023"
lower = 0
upper = 0
cnt = 0

print(len(s))

def timsaucon(str):
    n = len(s)
    ket_qua = "KHÔNG"
    min_len = n + 1

    for i in range(n):
        hoa = thuong = so = 0
        for j in range(i, n):
            c = s[j]
            if c.isupper():
                hoa = 1
            elif c.islower():
                thuong = 1
            elif c.isdigit():
                so = 1

            if hoa and thuong and so:
                do_dai = j - i + 1
                if do_dai < min_len:
                    min_len = do_dai
                    ket_qua = s[i:j+1]
                break  
    return ket_qua

for char in s:
    if char.isdigit():
        cnt += 1
    if char.islower():
        lower += 1
    if char.isupper():
        upper += 1
    
print(f"{upper} hoa, {lower} thường, {cnt} số")

print("Sâu con ngắn nhất là:", timsaucon(s))