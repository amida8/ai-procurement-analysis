# src/data_source.py
import pandas as pd

def load_supplier_data_lv1() -> pd.DataFrame:
    """
    Lv1：供应商基础数据来源（用于数据分析与可视化）

    业务背景：
    - 用于采购/供应链场景的供应商 KPI 分析
    - 后续可做：排序、可视化、评分模型（Lv2）

    字段说明（非常重要）：
    - supplier (str)
        供应商名称

    - pcs (int)
        当月 PCS 采购单量（订单/件数的量级指标，用于衡量规模）

    - on_time_48h (float)
        面辅料采购「分支阶段」48 小时准交率（%）
        说明：只看面辅料采购阶段，不是全链路交期
        例：95 表示 95%

    - bulk_lead_time_days (float)
        大货时效（天）
        说明：从下单到成品交付客户的「端到端」整体时效

    - return_rate (float)
        当月返修率（%）
        例：6.5 表示 6.5%
    """

    data = [
        {"supplier": "宇鑫布业", "pcs": 1340, "on_time_48h": 95.0, "bulk_lead_time_days": 6.6, "return_rate": 6.5},
        {"supplier": "义文纺织", "pcs": 1157, "on_time_48h": 96.0, "bulk_lead_time_days": 7.9, "return_rate": 8.2},
        {"supplier": "盈丰纺织", "pcs": 747,  "on_time_48h": 83.0, "bulk_lead_time_days": 14.9,"return_rate": 12.2},
        {"supplier": "润都布业", "pcs": 366,  "on_time_48h": 95.0, "bulk_lead_time_days": 7.2, "return_rate": 14.6},
        {"supplier": "新皇纺织", "pcs": 271,  "on_time_48h": 95.0, "bulk_lead_time_days": 9.0, "return_rate": 8.4},
    ]

    df = pd.DataFrame(data)

    # 可选：统一数据类型（更像真实项目）
    df["pcs"] = df["pcs"].astype(int)
    df["on_time_48h"] = df["on_time_48h"].astype(float)
    df["bulk_lead_time_days"] = df["bulk_lead_time_days"].astype(float)
    df["return_rate"] = df["return_rate"].astype(float)

    return df


if __name__ == "__main__":
    df = load_supplier_data_lv1()
    print(df)