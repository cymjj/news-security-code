import matplotlib.pyplot as plt

# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = ["省钱/性价比", "闲置变现", "环保理念", "寻找稀缺商品", "兴趣社交"]
sizes = [78, 65, 42, 28, 19]

plt.figure(figsize=(8,6))
plt.barh(labels, sizes, color="#4A90E2")
plt.xlabel("占比 (%)")
plt.title("二手交易动机占比（多选）（问卷样本 n=100）")

for index, value in enumerate(sizes):
    plt.text(value + 1, index, f"{value}%", va='center')

plt.tight_layout()
plt.show()
