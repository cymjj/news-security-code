import matplotlib.pyplot as plt

# 中文字体修复
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

age_groups = ['25岁及以下', '26-35岁', '36-45岁', '46岁以上']
age_values = [56.18, 25.55, 13.92, 4.35]

plt.figure(figsize=(8,5))
plt.bar(age_groups, age_values)

plt.title("二手交易用户年龄段占比")
plt.xlabel("年龄段")
plt.ylabel("占比（%）")

# 显示数值标签
for i, v in enumerate(age_values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center')

plt.tight_layout()
plt.show()
