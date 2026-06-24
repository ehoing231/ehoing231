def kiem_tra_so_nguyen_to(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không.
    
    Args:
        n: Số nguyên cần kiểm tra
        
    Returns:
        True nếu n là số nguyên tố, False nếu không
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Ví dụ sử dụng
    so_can_kiem_tra = 17
    if kiem_tra_so_nguyen_to(so_can_kiem_tra):
        print(f"{so_can_kiem_tra} là số nguyên tố.")
    else:
        print(f"{so_can_kiem_tra} không phải là số nguyên tố.")
    
    # Kiểm tra thêm một vài số khác
    test_numbers = [2, 10, 13, 25, 97]
    print("\nKiểm tra các số:")
    for num in test_numbers:
        result = "là" if kiem_tra_so_nguyen_to(num) else "không là"
        print(f"{num} {result} số nguyên tố")