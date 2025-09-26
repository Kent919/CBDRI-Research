"""
data_preprocessing.py - 数据清洗与标准化
"""
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from datetime import datetime

PROCESSED_DIR = "data/processed"
OUTPUT_SUFFIX = "_preprocessed.csv"

def load_and_clean():
    """加载并预处理三张表"""
    files = {
        "tls_meta": os.path.join(PROCESSED_DIR, "tls_meta.csv"),
        "container_call": os.path.join(PROCESSED_DIR, "container_call.csv"),
        "icc_lookup": os.path.join(PROCESSED_DIR, "icc_lookup.csv")
    }
    
    dfs = {}
    for name, path in files.items():
        print(f"🧹 加载并清洗 {name}...")
        df = pd.read_csv(path)
        
        # 异常值过滤
        if name == "tls_meta":
            df = df[(df["ch_len"] > 100) & (df["ch_len"] < 1500)]
            cols = ["ch_len", "cipher_suites", "up_packet_count", "down_packet_count", "avg_inter_arrival"]
            scaler = StandardScaler()
            df[cols] = scaler.fit_transform(df[cols])
        
        elif name == "container_call":
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df = df.dropna(subset=["timestamp"])
            df = df[df["call_freq_in_5min"] >= 1]
        
        # 保存
        output_path = os.path.join(PROCESSED_DIR, name + OUTPUT_SUFFIX)
        df.to_csv(output_path, index=False)
        dfs[name] = df
        print(f"✅ 保存预处理后数据 → {output_path}")
    
    return dfs

if __name__ == "__main__":
    processed_dfs = load_and_clean()
    print("🎉 数据预处理完成！")