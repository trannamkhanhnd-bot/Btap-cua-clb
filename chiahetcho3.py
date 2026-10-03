t = int(input())

# Vòng lặp chạy qua từng bộ test
for _ in range(t):
    # Đọc số N dưới dạng một chuỗi (string) vì nó quá dài (lên tới 500 chữ số)
    s = input()
    
    # Biến để tính tổng các chữ số
    tong_chu_so = 0
    
    # Dùng vòng lặp for duyệt qua từng ký tự (chữ số) trong chuỗi s
    for ky_tu in s:
        # Chuyển ký tự số thành số nguyên rồi cộng dồn vào tổng
        tong_chu_so = tong_chu_so + int(ky_tu)
        
    # Kiểm tra xem tổng các chữ số có chia hết cho 3 hay không (dùng phép chia lấy dư %)
    if tong_chu_so % 3 == 0:
        print("YES")
    else:
        print("NO")