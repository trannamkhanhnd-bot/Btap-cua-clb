t = int(input())

# Vòng điều khiển các bộ test
for _ in range(t):
    # Đọc số lượng phần tử n của mảng
    n = int(input())
    
    # Đọc dòng tiếp theo chứa các số của mảng A[], chuyển thành danh sách số nguyên (list)
    a = list(map(int, input().split()))
    
    # Gán giá trị ban đầu cực kỳ lớn cho số nhỏ nhất và nhỏ thứ hai
    nho_nhat = float('inf')
    nho_thu_hai = float('inf')
    
    # Duyệt qua từng số trong mảng bằng vòng lặp for
    for x in a:
        if x < nho_nhat:
            # Nếu tìm thấy số nhỏ hơn số nhỏ nhất hiện tại:
            # Số nhỏ nhất cũ tụt xuống làm số nhỏ thứ hai
            nho_thu_hai = nho_nhat
            # Cập nhật số nhỏ nhất mới
            nho_nhat = x
        elif x > nho_nhat and x < nho_thu_hai:
            # Nếu số này lớn hơn số nhỏ nhất nhưng lại nhỏ hơn số nhỏ thứ hai hiện tại
            nho_thu_hai = x
            
    # Kiểm tra kết quả sau khi duyệt xong
    # Nếu nho_thu_hai vẫn là vô cùng (nghĩa là không tìm được số thứ hai khác biệt)
    if nho_thu_hai == float('inf'):
        print(-1)
    else:
        print(nho_nhat, nho_thu_hai)