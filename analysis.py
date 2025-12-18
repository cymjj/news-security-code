# -*- coding: utf-8 -*-
"""
二手问卷交叉分析脚本
---------------------------------
需要的库：
pip install pandas numpy matplotlib scipy openpyxl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import matplotlib

# ==== 中文字体设置（关键）====
# Windows 推荐使用 SimHei 或 Microsoft YaHei
matplotlib.rcParams['font.sans-serif'] = ['SimHei']       # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False         # 解决负号显示为方块的问题
# =============================


# ========= 1. 读入数据 =========
# 请把文件名改成你自己的 Excel 文件名
file_path = "survey.xlsx"
df = pd.read_excel(file_path)

# 如果列名跟这里不一样，请对应修改
# 期望的列：
# age_group, city_level, used_platform, use_freq, main_motive, trust_score, fav_platform

# ========= 2. 一些中文标签映射（方便图表好看） =========
age_labels = {
    1: "18–22岁",
    2: "23–30岁",
    3: "31岁及以上"
}

used_labels = {
    0: "从未使用",
    1: "使用过"
}

motive_labels = {
    1: "省钱/性价比",
    2: "闲置变现",
    3: "环保理念",
    4: "兴趣/社交"
}

# ========= 3. 交叉分析一：年龄 × 是否使用二手平台 =========

# 3.1 列联表（频数）
ct1 = pd.crosstab(df["age_group"], df["used_platform"])
print("【年龄 × 是否使用二手平台】列联表（频数）")
print(ct1)

# 3.2 行百分比（每个年龄段内部的使用率）
ct1_pct = ct1.div(ct1.sum(axis=1), axis=0) * 100
print("\n【年龄 × 是否使用二手平台】行百分比（%）")
print(ct1_pct.round(2))

# 3.3 卡方检验
chi2_1, p_1, dof_1, expected_1 = chi2_contingency(ct1)
print("\n【年龄 × 是否使用二手平台】卡方检验结果")
print(f"chi2 = {chi2_1:.3f}, df = {dof_1}, p-value = {p_1:.4f}")

# 3.4 画分组条形图（展示百分比）
fig, ax = plt.subplots(figsize=(7, 5))

# 让索引和列都换成中文
plot_df1 = ct1_pct.copy()
plot_df1.index = [age_labels[i] for i in plot_df1.index]
plot_df1.columns = [used_labels[j] for j in plot_df1.columns]

plot_df1.plot(kind="bar", ax=ax)

ax.set_xlabel("年龄段")
ax.set_ylabel("占比（%）")
ax.set_title("不同年龄段二手平台使用情况")
ax.set_ylim(0, 100)
ax.legend(title="是否使用二手平台")

# 在柱子上标数字
for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%", fontsize=8)

plt.tight_layout()
plt.savefig("age_vs_used_platform.png", dpi=300)
plt.close()
print("\n图表已保存：age_vs_used_platform.png")

# ========= 4. 交叉分析二：使用频率分组 × 主要动机 =========

# 4.1 先创建一个“频率分组”变量：高频 vs 低频
# use_freq: 1=几乎从不; 2=一年几次; 3=每月1次; 4=每月多次
df["freq_group"] = np.where(df["use_freq"] >= 3,
                            "高频（≥每月1次）",
                            "低频（＜每月1次）")

# 4.2 列联表（频数）
ct2 = pd.crosstab(df["freq_group"], df["main_motive"])
print("\n【使用频率分组 × 主要动机】列联表（频数）")
print(ct2)

# 4.3 行百分比
ct2_pct = ct2.div(ct2.sum(axis=1), axis=0) * 100
print("\n【使用频率分组 × 主要动机】行百分比（%）")
print(ct2_pct.round(2))

# 4.4 卡方检验
chi2_2, p_2, dof_2, expected_2 = chi2_contingency(ct2)
print("\n【使用频率分组 × 主要动机】卡方检验结果")
print(f"chi2 = {chi2_2:.3f}, df = {dof_2}, p-value = {p_2:.4f}")

# 4.5 画堆叠条形图（100% 堆叠）
fig, ax = plt.subplots(figsize=(7, 5))

plot_df2 = ct2_pct.copy()
plot_df2.columns = [motive_labels[k] for k in plot_df2.columns]

plot_df2.plot(kind="bar", stacked=True, ax=ax)

ax.set_xlabel("使用频率分组")
ax.set_ylabel("构成比例（%）")
ax.set_title("不同使用频率用户的主要动机对比")
ax.set_ylim(0, 100)
ax.legend(title="主要使用动机", bbox_to_anchor=(1.02, 1), loc="upper left")

# 在堆叠条形图上标百分比（可选）
for c in ax.containers:
    ax.bar_label(c, fmt="%.1f%%", label_type="center", fontsize=7)

plt.tight_layout()
plt.savefig("freqgroup_vs_motive.png", dpi=300)
plt.close()
print("图表已保存：freqgroup_vs_motive.png")

