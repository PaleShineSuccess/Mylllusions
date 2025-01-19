import matplotlib.pyplot as plt
import numpy as np

#字符顏色
c1=(197, 35, 137)
c2=(255, 255, 255)
#棋盤顏色
color1 = (160, 215, 51)
color2 = (79, 187, 129)

def rgb_to_float(rgb):
    return tuple(color / 255 for color in rgb)

def draw_checkerboard(ax, rows, cols, size):
# 繪製方塊
    for row in range(rows):
        for col in range(cols):
            color = rgb_to_float(color1) if (row + col) % 2 == 0 else rgb_to_float(color2)
            square = plt.Rectangle((col * size, row * size), size, size, color=color)
            ax.add_artist(square)

# 棋盤設置
checkerboard_rows = 18  # 行數
checkerboard_cols = checkerboard_rows  # 列數，目前設置和行數一致
square_size = 8  # 方格大小

# 其他自定義參數
x = checkerboard_rows - 2  # 每行顯示的字符數量
max_rows = checkerboard_rows - 2  # 最大顯示的字符行數
char_to_display = '✚'  # 顯示的字符
font_size = 20  # 字符大小
dot_spacing = 8  # 字符間距

# 圖像設置
width = x * dot_spacing + square_size  # 根據使用者定義的字符數量設置寬度
height = min(max_rows, checkerboard_rows) * dot_spacing + square_size  # 根據最大行數設置高度

# 定義顏色模式（使用 RGB 代碼）
pattern = '0110100101101001'
colors = [c1 if bit == '1' else c2 for bit in pattern]  # 粉色和白色

# 創建圖像
fig, ax = plt.subplots(figsize=(width / 15, height / 15))

# 繪製棋盤
draw_checkerboard(ax, checkerboard_rows, checkerboard_cols, size=square_size)

# 繪製字符
for row in range(min(max_rows, checkerboard_rows)):  # 限制行數
    for col in range(x):  # 只顯示前 x 個字符
        if col < checkerboard_cols:  # 確保不超出列數
            x_coord = (col) * dot_spacing + dot_spacing / 2 + 4  # 每行字符前移一位
            y_coord = height - (row * dot_spacing) - dot_spacing / 2 - 4.95  # 調整 y 坐標

            # 根據行數計算顏色，實現每行後移一位
            color_index = (col - row) % len(colors)
            color = rgb_to_float(colors[color_index])  # 將 RGB 轉換為浮點數

            # 使用 text 方法顯示字符
            ax.text(x_coord, y_coord, char_to_display, fontsize=font_size, ha='center', va='center', color=color)

# 設置坐標軸
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')
ax.axis('off')  # 不顯示坐標軸

# 顯示圖像
plt.show()
