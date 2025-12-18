import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体（解决乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']     # 中文黑体
plt.rcParams['axes.unicode_minus'] = False       # 解决中文负号乱码

# 数据
years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
users = np.array([0.49, 1.07, 2.52, 3.23, 4.63, 5.8, 6.6]) 
penetration = np.array([5.91, 12.53, 25.48, 31.30, 43.38, 53.75, 60.0])

fig, ax1 = plt.subplots(figsize=(8, 5))

# 柱状图（用户规模）
ax1.bar(years, users, width=0.6, color="#4B8BBE")
ax1.set_xlabel("年份")
ax1.set_ylabel("二手电商用户规模（亿人）")

# 折线图（渗透率）
ax2 = ax1.twinx()
ax2.plot(years, penetration, marker="o", color="#FF9900")
ax2.set_ylabel("渗透率（%）")

plt.title("2018-2024年中国二手电商用户规模及渗透率趋势")
plt.tight_layout()
plt.show()
