# 📊 Supplier KPI Dashboard（Python × データ可視化）

## 概要 / Overview

本プロジェクトは、  
**既存の仕入先（サプライヤー）KPIデータを Python で可視化・分析し、  
調達判断に役立つ示唆を得ること** を目的としたデータ分析作品です。

CSV / Excel ファイルをアップロードするだけで、  
仕入先の **納期・品質・取引規模** を即座に可視化できる  
シンプルなダッシュボードを実装しています。

---

## 🎯 目的 / Objective

- 既に存在する仕入先データを活用し  
- Python を用いてデータを構造化・可視化し  
- 調達・仕入判断の補助となる情報を提供する  
本ダッシュボードは、  
属人的になりがちな仕入判断を  
可視化・共通認識化することを目的としています。

👉 **分析のための分析ではなく、実務利用を想定した設計です。**

---

## 🗂 データ内容 / Data Description

本ダッシュボードでは、以下の指標を使用します。

| カラム名 | 内容 |
|---|---|
| supplier | 仕入先名 |
| pcs | 当月の調達数量（PCS） |
| on_time_48h | 面辅料調達工程における48時間以内の納期遵守率（％） |
| bulk_lead_time_days | 注文から成品を顧客へ納品するまでの全体リードタイム（日） |
| return_rate | 当月の返修率（％） |

※ `on_time_48h` は **全体納期ではなく、面辅料調達分岐工程のみ** を対象としています。

---

## 📈 可視化内容 / Visualization

ダッシュボードでは以下を表示します。

1. **PCS（調達数量）ランキング**  
2. **48h 納期遵守率ランキング（面辅料工程）**  
3. **品質 × スピード 分析**  
   - 返修率（品質）  
   - 大貨リードタイム（スピード）  
4. **リスク分類（Lv1 ルール）**  
   - LOW / MEDIUM / HIGH  

---
## 🧠 自動分析 / Auto Insights（Lv1）

以下の業務ルールにより自動判定しています。

- **優先候補（Top3）**
  - PCS が高い
  - 納期遵守率 ≥ 95%
  - 返修率 ≤ 3%

- **要注意仕入先（HIGH）**
  - 納期遵守率 < 90%
  - または 返修率 > 5%

---

## 🛠 使用技術 / Tech Stack

- Python  
- pandas  
- matplotlib  
- Streamlit  


---


## 🚀 実行方法 / How to Run

```bash
pip install streamlit pandas matplotlib
streamlit run app.py
```

---

## 🖥 プレビュー / Demo

🔗

---

## 📁 ファイル構成 / File Structure

```text
supplier-kpi-dashboard/
├── app.py
├── data/
│   └── sample_supplier_kpi.csv
├── requirements.txt
└── README.md
```

---

## 👤 作者 / Author

- Name: リナ（LI NA）  
- Email: nina1769796516@gmail.com  
- 背景：アパレル業界での調達・サプライヤー管理経験
- 本作品では 実務経験を活かしたデータ分析 を重視しています。

---

## 📄 ライセンス / License

MIT License



