# -*- coding: utf-8 -*-
"""
二手经济市场规模：CAGR 计算 + 2025–2028 趋势外推
运行环境：Python 3.x
需要库：pandas、numpy、matplotlib
pip install pandas numpy matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# ------------ 1. 中文字体设置（非常重要）-------------
# Windows 推荐 SimHei 或 Microsoft YaHei
matplotlib.rcParams['font.sans-serif'] = ['SimHei']       # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False         # 解决负号显示问题
# ---------------------------------------------------

# ------------ 2. 输入历史数据（单位：万亿元）------------

# 年份（2019–2024）
years_hist = np.array([2019, 2020, 2021, 2022, 2023, 2024])


values_hist = np.array([0.95, 1.05, 1.15, 1.25, 1.35, 1.40])  # 单位：万亿元

# ------------ 3. 计算 CAGR（复合年均增长率）------------

n_years = len(years_hist) - 1          # 间隔年数，这里是 5
cagr = (values_hist[-1] / values_hist[0]) ** (1 / n_years) - 1

print("==== 2019–2024 年二手经济市场规模 ====")
for y, v in zip(years_hist, values_hist):
    print(f"{y} 年：{v:.2f} 万亿元")
print(f"\n2019–2024 年复合年均增长率 CAGR ≈ {cagr:.2%}\n")

# ------------ 4. 按 CAGR 外推 2025–2028 ------------

years_fore = np.arange(2025, 2029)   # 2025–2028
values_fore = [values_hist[-1] * (1 + cagr) ** i
               for i in range(1, len(years_fore) + 1)]

print("==== 按 CAGR 趋势外推的 2025–2028 市场规模（示意） ====")
for y, v in zip(years_fore, values_fore):
    print(f"{y} 年：{v:.2f} 万亿元")

# 组合成一张表，方便复制到论文 / Excel
df_all = pd.DataFrame({
    "年份": np.concatenate([years_hist, years_fore]),
    "历史值_万亿元": list(values_hist) + [np.nan] * len(years_fore),
    "预测值_万亿元": [np.nan] * len(years_hist) + list(values_fore),
})
print("\n==== 汇总表（历史 + 预测） ====")
print(df_all)

# ------------ 5. 画“历史 + 预测”折线图 ------------

plt.figure(figsize=(8, 5))

# 历史值：实线
plt.plot(years_hist, values_hist,
         marker="o", linestyle="-", label="历史值")

# 预测值：虚线
plt.plot(years_fore, values_fore,
         marker="o", linestyle="--", label="预测值（趋势外推）")

plt.xlabel("年份")
plt.ylabel("市场规模（万亿元）")
plt.title("中国二手经济市场规模及趋势外推（2019–2028）")
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig("secondhand_market_forecast_2019_2028.png", dpi=300)
plt.show()

print("\n图已保存为：secondhand_market_forecast_2019_2028.png")
