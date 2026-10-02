t = int(input())
while t > 0:
    dong_1 = input().split()
    n = int(dong_1[0])
    x = int(dong_1[1])
    chuoi_mang = input().split()
    a = []
    for i in range(n):
        so_nguyen = int(chuoi_mang[i])
        a.append(so_nguyen)
    ket_qua = -1
    for j in range(n):
        if a[j] == x:
            ket_qua = 1
            break
    print(ket_qua) 