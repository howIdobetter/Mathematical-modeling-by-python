import numpy as np
import matplotlib.pyplot as plt

# === 参数设置 ===
GRID_SIZE = 100  # 网格大小 (100x100)
UPDATE_INTERVAL = 0.1  # 更新间隔（秒）

# === 初始化网格 ===
# 创建一个全零的二维数组，表示初始状态（0=死，1=活）
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# 设置初始模式（例如：滑翔机 Glider）
grid[1][2] = 1
grid[2][3] = 1
grid[3][1] = 1
grid[3][2] = 1
grid[3][3] = 1

# === 图像显示配置 ===
plt.ion()  # 开启交互模式
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary', interpolation='nearest')  # 使用二值颜色
ax.set_title("Conway's Game of Life")
plt.axis('off')  # 隐藏坐标轴


# === 核心逻辑函数 ===
def update_grid(old_grid):
    """
    根据生命游戏规则更新网格状态
    规则：
    1. 活细胞周围有2或3个活细胞 -> 存活
    2. 活细胞周围少于2或多于3个活细胞 -> 死亡
    3. 死细胞周围恰好3个活细胞 -> 复活
    """
    new_grid = old_grid.copy()

    # 计算每个细胞的邻居数量（使用卷积核）
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    neighbor_counts = convolve2d(old_grid, kernel, mode='same', boundary='wrap')

    # 应用规则更新网格
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # 活细胞规则
            if old_grid[i][j] == 1:
                if neighbor_counts[i][j] < 2 or neighbor_counts[i][j] > 3:
                    new_grid[i][j] = 0
            # 死细胞规则
            else:
                if neighbor_counts[i][j] == 3:
                    new_grid[i][j] = 1
    return new_grid


# === 主循环 ===
try:
    while True:
        grid = update_grid(grid)  # 更新网格状态
        img.set_data(grid)  # 更新图像数据
        plt.pause(UPDATE_INTERVAL)  # 暂停指定时间
        fig.canvas.flush_events()  # 强制刷新界面
except KeyboardInterrupt:
    plt.ioff()  # 关闭交互模式
    plt.show()  # 显示最终图像