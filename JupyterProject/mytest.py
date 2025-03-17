def is_good_number(num):
    num_str = str(num)
    # 从低位到高位检查每一位
    for i, digit in enumerate(reversed(num_str)):
        if i % 2 == 0:  # 奇数位 (注意：从 0 开始，所以 0, 2, 4... 是个位、百位...)
            if int(digit) % 2 != 1:
                return False
        else:  # 偶数位 (1, 3, 5... 是十位、千位...)
            if int(digit) % 2 != 0:
                return False
    return True

good_numbers = [num for num in range(1, 2025) if is_good_number(num)]
print(good_numbers)
print(len(good_numbers))