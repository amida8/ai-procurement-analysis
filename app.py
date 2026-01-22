# app.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import sys

# ======================
# Path / Import
# ======================
BASE = Path(__file__).resolve().parent
SRC = BASE / "src"
sys.path.append(str(SRC))

from data_source import load_supplier_data_lv1  # サンプルデータ

# ======================
# Page config
# ======================
st.set_page_config(page_title="Supplier KPI Dashboard", layout="wide")

st.title("📊 Supplier KPI Dashboard（Lv1）")
st.caption("CSV / Excel をアップロードすると、即座に可視化・分析します")

# ======================
# Upload area
# ======================
st.sidebar.header("📂 データアップロード")
uploaded_file = st.sidebar.file_uploader(
    "CSV または Excel を選択",
    type=["csv", "xlsx"]
)

# ======================
# Load data
# ======================
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.sidebar.success("アップロード成功 ✅")
else:
    df = load_supplier_data_lv1()
    st.sidebar.info("※ サンプルデータを使用中")

# ======================
# Required columns check
# ======================
required_cols = {
    "supplier",
    "pcs",
    "on_time_48h",
    "bulk_lead_time_days",
    "return_rate"
}

missing = required_cols - set(df.columns)
if missing:
    st.error(f"❌ 必要なカラムが不足しています: {missing}")
    st.stop()

# ======================
# Risk classification (Lv1)  ★必ず先に作る
# ======================
def risk(row):
    if row["on_time_48h"] < 90 or row["return_rate"] > 15:
        return "HIGH"
    if row["on_time_48h"] < 93 or row["return_rate"] > 10:
        return "MEDIUM"
    return "LOW"

df["risk"] = df.apply(risk, axis=1)

# ======================
# KPI cards
# ======================
c1, c2, c3, c4 = st.columns(4)
c1.metric("仕入先数", len(df))

c2.metric(
    "48時間以内 納期遵守率",
    f"{df['on_time_48h'].mean():.1f}%"
)
c2.caption("（平均）")

c3.metric(
    "再加工率",
    f"{df['return_rate'].mean():.1f}%"
)
c3.caption("（平均）")

c4.metric(
    "全体リードタイム",
    f"{df['bulk_lead_time_days'].mean():.1f} 日"
)
c4.caption("（平均）")

st.divider()

# ======================
# Charts
# ======================
left, right = st.columns(2)

with left:
    st.subheader("① PCS（当月調達数量）ランキング")
    d = df.sort_values("pcs", ascending=False)
    fig = plt.figure(figsize=(8, 4))
    plt.bar(d["supplier"], d["pcs"])
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("PCS")
    plt.tight_layout()
    st.pyplot(fig)

with right:
    st.subheader("② 副資材調達：48時間以内 納期遵守率")
    d = df.sort_values("on_time_48h", ascending=False)
    fig = plt.figure(figsize=(8, 4))
    plt.bar(d["supplier"], d["on_time_48h"])
    plt.ylim(0, 100)
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("％")
    plt.tight_layout()
    st.pyplot(fig)

left2, right2 = st.columns(2)

with left2:
    st.subheader("③ 品質 × リードタイム")
    fig = plt.figure(figsize=(8, 4))

    for _, r in df.iterrows():
        color = "#F44336" if r["risk"] == "HIGH" else "#2196F3"
        plt.scatter(
            r["bulk_lead_time_days"],
            r["return_rate"],
            color=color
        )
        plt.text(
            r["bulk_lead_time_days"],
            r["return_rate"],
            r["supplier"],
            fontsize=9
        )

    plt.xlabel("E2E リードタイム（日）")
    plt.ylabel("不良率(%)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

with right2:
    st.subheader("④ リスク分類（一次判定ルール）")

    counts = df["risk"].value_counts()

    color_map = {
        "LOW": "#4CAF50",
        "MEDIUM": "#FFC107",
        "HIGH": "#F44336"
    }
    colors = [color_map[i] for i in counts.index]

    fig = plt.figure(figsize=(8, 4))
    plt.bar(counts.index, counts.values, color=colors)
    plt.ylabel("件数")
    plt.tight_layout()
    st.pyplot(fig)

st.divider()

# ======================
# Auto insights
# ======================
st.subheader("🧠 自動分析結果")

df["score"] = (
    (df["on_time_48h"] / 100) * 0.5 +
    (1 - df["return_rate"] / 100) * 0.3 +
    (1 / df["bulk_lead_time_days"]) * 0.2
)

top3 = df.sort_values("score", ascending=False).head(3)
risk_high = df[df["risk"] == "HIGH"]

c1, c2 = st.columns(2)
with c1:
    st.markdown("✅ **優先候補 Top3**")
    st.dataframe(
        top3[["supplier", "on_time_48h", "return_rate", "bulk_lead_time_days", "pcs"]]
    )

with c2:
    st.markdown("⚠️ **要注意（HIGH）**")
    if len(risk_high) == 0:
        st.write("該当なし")
    else:
        st.dataframe(
            risk_high[["supplier", "on_time_48h", "return_rate", "bulk_lead_time_days", "pcs"]]
        )

st.divider()
st.subheader("📄 生データ")
st.dataframe(df)