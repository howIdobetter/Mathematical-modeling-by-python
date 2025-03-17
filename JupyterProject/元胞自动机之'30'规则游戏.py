import time

def cellular_automaton(rule=30, generations=20, init_cell='1'):
    """
    一维元胞自动机模拟（基于规则 30）
    :param rule: 规则号（0-255）
    :param generations: 演化的代数
    :param init_cell: 初始状态的中心元胞（例如 '1' 或 '0'）
    """
    # 将规则转换为二进制（8位），例如规则30 -> '00011110'
    rule_bin = format(rule, '08b')
    rule_dict = {
        (7 - i): int(bit) for i, bit in enumerate(rule_bin)
    }

    # 初始化第一代（中心为1，其余为0）
    width = 2 * generations + 1  # 确保足够宽度显示所有演化
    cells = ['0'] * width
    cells[width // 2] = init_cell  # 中心元胞初始状态

    # 演化过程
    for _ in range(generations):
        print(''.join(cells).replace('0', ' ').replace('1', '█'))
        new_cells = ['0'] * width
        for i in range(1, width - 1):
            # 获取当前元胞及其左右邻居的状态（转换为整数）
            left = cells[i - 1]
            current = cells[i]
            right = cells[i + 1]
            key = int(left + current + right, 2)  # 三位二进制转十进制（0-7）
            new_cells[i] = str(rule_dict[key])
        cells = new_cells
        time.sleep(0.1)

if __name__ == "__main__":
    cellular_automaton(rule = 30, generations=20, init_cell='1')