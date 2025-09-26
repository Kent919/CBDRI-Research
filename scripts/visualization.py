"""
visualization.py - 生成 ICC 热力图等图表
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Arial', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

PROCESSED_DIR = "data/processed"
FIGURES_DIR = "docs/figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

def plot_icc_heatmap():
    """绘制 ICC 热力图"""
    df = pd.read_csv(os.path.join(PROCESSED_DIR, "icc_lookup.csv"))
    df.set_index("region", inplace=True)
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(df[["ICC_cr_gdpr"]].T, annot=True, cmap="Blues", fmt=".2f")
    plt.title("制度耦合系数 (ICC) 热力图")
    plt.ylabel("")
    plt.tight_layout()
    
    output = os.path.join(FIGURES_DIR, "icc_heatmap.png")
    plt.savefig(output, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"🎨 热力图已保存 → {output}")

if __name__ == "__main__":
    plot_icc_heatmap()