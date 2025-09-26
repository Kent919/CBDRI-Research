# CBDRI
Cross-Border Data Risk Index 
# CBDRI-Research 安装与运行指南

## 本地运行

```bash
git clone https://github.com/Kent919/CBDRI-Research.git
cd CBDRI-Research
pip install -r requirements.txt

# 依次运行
python scripts/data_collection.py
python scripts/data_preprocessing.py
python scripts/model_training.py
python scripts/visualization.py
