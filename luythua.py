MOD = 1000000007

# Hàm tính lũy thừa nhanh (Lũy thừa nhị phân)
def tinh_luy_thua(n, k):
    ket_qua = 1
    n = n % MOD  # Rút gọn n trước nếu n quá lớn
    
    # Dùng vòng lặp while để thu nhỏ dần số mũ k
    while k > 0:
        # Nếu k là số lẻ (kiểm tra bằng phép chia dư k % 2 == 1)
        if k % 2 == 1:
            ket_qua = (ket_qua * n) % MOD
            
        # Bình phương cơ số n lên và chia đôi số mũ k cho 2
        n = (n * n) % MOD
        k = k // 2
        
    return ket_qua

# Đọc số lượng bộ test T
t = int(input())

# Vòng lặp xử lý từng bộ test
for _ in range(t):
    # Đọc hai số N và K trên cùng một dòng
    n, k = map(int, input().split())
    
    # Gọi hàm tính và in ra kết quả
    print(tinh_luy_thua(n, k))