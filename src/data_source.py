# src/data_source.py
import pandas as pd

def load_supplier_data_lv1() -> pd.DataFrame:
    """
    Lv1：仕入先（サプライヤー）KPI 基礎データ

    【目的】
    - 調達・サプライチェーン領域における仕入先評価
    - Python によるデータ分析・可視化の基礎データとして利用
    - 将来的にスコアリング／機械学習へ拡張可能（Lv2 以降）

    【カラム説明】

    supplier : str  
        仕入先名

    pcs : int  
        当月の PCS 調達数量  
        （取引規模・取引量を示す指標）

    on_time_48h : float  
        面辅料（付属・生地）調達工程における  
        「48時間以内 納期遵守率（％）」  
        ※ 全体納期ではなく、調達分岐工程のみを対象

    bulk_lead_time_days : float  
        大貨リードタイム（日）  
        注文確定から製品が顧客へ納品されるまでの  
        エンドツーエンドの全体所要日数

    return_rate : float  
        当月の返修率（％）  
        品質安定性を示す指標
    """

    data = [
        {"supplier": "宇鑫布業", "pcs": 1340, "on_time_48h": 95.0, "bulk_lead_time_days": 6.6, "return_rate": 6.5},
        {"supplier": "義文紡織", "pcs": 1157, "on_time_48h": 96.0, "bulk_lead_time_days": 7.9, "return_rate": 8.2},
        {"supplier": "盈豊紡織", "pcs": 747,  "on_time_48h": 83.0, "bulk_lead_time_days": 14.9,"return_rate": 12.2},
        {"supplier": "潤都布業", "pcs": 366,  "on_time_48h": 95.0, "bulk_lead_time_days": 7.2, "return_rate": 14.6},
        {"supplier": "新皇紡織", "pcs": 271,  "on_time_48h": 95.0, "bulk_lead_time_days": 9.0, "return_rate": 8.4},
    ]

    df = pd.DataFrame(data)

    # データ型を明示（実務向け）
    df["pcs"] = df["pcs"].astype(int)
    df["on_time_48h"] = df["on_time_48h"].astype(float)
    df["bulk_lead_time_days"] = df["bulk_lead_time_days"].astype(float)
    df["return_rate"] = df["return_rate"].astype(float)

    return df


if __name__ == "__main__":
    df = load_supplier_data_lv1()
    print(df)