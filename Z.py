import matplotlib.pyplot as plt

# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
z_value = 56.18
non_z_value = 100 - z_value

labels = ['Z世代（25岁及以下）', '其他年龄段']
sizes = [z_value, non_z_value]
colors = ['#4a90e2', '#f5a623']

# 创建画布（更小的边距，更专业）
fig, ax = plt.subplots(figsize=(7,7))

# 绘制环形图
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,               # 不自动加标签（防止超出画布）
    autopct='%1.1f%%',
    pctdistance=0.8,          # 百分比位置靠内
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.35, edgecolor='white')
)

# 百分比文本样式
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(14)
    autotext.set_weight('bold')

# 添加外部分组标签（可控且不会溢出）
ax.text(-1.1, 0, labels[0], fontsize=14, va='center', ha='right')
ax.text(1.1, 0, labels[1], fontsize=14, va='center', ha='left')

# 中心标题（小而居中）
plt.text(0, 0, "Z世代\n占比", ha='center', va='center',
         fontsize=16, fontweight='bold')

# 主标题
plt.title("二手交易用户中 Z世代占比（核心群体）",
          fontsize=17, fontweight='bold', pad=20)

# 保持圆形
ax.set_aspect('equal')

# 自动修正布局防止任何内容被遮挡
plt.tight_layout()

plt.show()
