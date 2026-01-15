# src/visualize_lv1.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from data_source import load_supplier_data_lv1


def ensure_outputs_dir() -> Path:
    out = Path(__file__).resolve().parents[1] / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    return out


def plot_bar_top_pcs(df: pd.DataFrame, out_dir: Path) -> None:
    # PCS Top（取引量ランキング）
    df2 = df.sort_values("pcs", ascending=False)

    plt.figure(figsize=(10, 5))
    plt.bar(df2["supplier"], df2["pcs"])
    plt.title("PCS（当月調達数量）ランキング")
    plt.xlabel("仕入先")
    plt.ylabel("PCS")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "01_pcs_ranking.png", dpi=200)
    plt.close()


def plot_scatter_quality_vs_speed(df: pd.DataFrame, out_dir: Path) -> None:
    # 返修率（低いほど良い） vs 大貨リードタイム（短いほど良い）
    plt.figure(figsize=(7, 5))
    plt.scatter(df["bulk_lead_time_days"], df["return_rate"])
    for _, r in df.iterrows():
        plt.text(r["bulk_lead_time_days"], r["return_rate"], r["supplier"], fontsize=9)

    plt.title("品質(返修率) × スピード(大貨リードタイム)")
    plt.xlabel("大貨リードタイム（日）※短いほど良い")
    plt.ylabel("返修率（％）※低いほど良い")
    plt.tight_layout()
    plt.savefig(out_dir / "02_quality_vs_speed.png", dpi=200)
    plt.close()


def plot_on_time_48h(df: pd.DataFrame, out_dir: Path) -> None:
    # 面辅料調達工程：48h 納期遵守率（高いほど良い）
    df2 = df.sort_values("on_time_48h", ascending=False)

    plt.figure(figsize=(10, 5))
    plt.bar(df2["supplier"], df2["on_time_48h"])
    plt.title("面辅料調達工程：48h 納期遵守率（％）ランキング")
    plt.xlabel("仕入先")
    plt.ylabel("48h 納期遵守率（％）")
    plt.ylim(0, 100)
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "03_on_time_48h_ranking.png", dpi=200)
    plt.close()


def main():
    df = load_supplier_data_lv1()
    out_dir = ensure_outputs_dir()

    plot_bar_top_pcs(df, out_dir)
    plot_scatter_quality_vs_speed(df, out_dir)
    plot_on_time_48h(df, out_dir)

    print("✅ 完了：outputs/ に画像を保存しました")
    print(" - 01_pcs_ranking.png")
    print(" - 02_quality_vs_speed.png")
    print(" - 03_on_time_48h_ranking.png")


if __name__ == "__main__":
    main()