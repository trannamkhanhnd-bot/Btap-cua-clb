n = int(input())
luoi = []
for i in range(n):
    dong = input()
    luoi.append(dong)

tong_so_cap = 0
for i in range(n):          
    dem_c = 0              
    for j in range(n):      
        if luoi[i][j] == 'C':
            dem_c = dem_c + 1  
        else:
            pass
    if dem_c >= 2:
        so_cap_hang = dem_c * (dem_c - 1) // 2
        tong_so_cap = tong_so_cap + so_cap_hang
    else:
        pass
for j in range(n):          # Cố định cột j
    dem_c = 0               # Biến đếm số chữ 'C' trong cột hiện tại
    for i in range(n):      # Duyệt qua từng hàng i của cột đó
        if luoi[i][j] == 'C':
            dem_c = dem_c + 1  # Nếu là chữ 'C' thì tăng biến đếm lên 1
        else:
            pass
            
    # Nếu cột này có từ 2 đồng xu trở lên thì mới tạo được cặp
    if dem_c >= 2:
        so_cap_col = dem_c * (dem_c - 1) // 2
        tong_so_cap = tong_so_cap + so_cap_col
    else:
        pass
print(tong_so_cap)