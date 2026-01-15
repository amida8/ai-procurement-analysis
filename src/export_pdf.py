# src/export_pdf.py
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime


def export_supplier_report_pdf(
    output_path: Path,
    summary: dict,
    top_suppliers: list,
    risk_suppliers: list
):
    """
    生成 供应商 KPI 分析 PDF 报告（Lv1）
    """

    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    # ---- Title ----
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2 * cm, height - 2 * cm, "Supplier KPI Analysis Report")

    c.setFont("Helvetica", 10)
    c.drawString(2 * cm, height - 2.8 * cm, f"Generated at: {datetime.now():%Y-%m-%d %H:%M}")

    y = height - 4 * cm

    # ---- Summary ----
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "1. Summary")
    y -= 0.8 * cm

    c.setFont("Helvetica", 10)
    for k, v in summary.items():
        c.drawString(2.5 * cm, y, f"- {k}: {v}")
        y -= 0.6 * cm

    y -= 0.6 * cm

    # ---- Top Suppliers ----
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "2. Recommended Suppliers (Top)")
    y -= 0.8 * cm

    c.setFont("Helvetica", 10)
    for s in top_suppliers:
        c.drawString(
            2.5 * cm,
            y,
            f"- {s['supplier']} | 48h: {s['on_time_48h']}% | Return: {s['return_rate']}% | LeadTime: {s['bulk_lead_time_days']} days"
        )
        y -= 0.6 * cm

    y -= 0.6 * cm

    # ---- Risk Suppliers ----
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "3. High Risk Suppliers")
    y -= 0.8 * cm

    c.setFont("Helvetica", 10)
    if not risk_suppliers:
        c.drawString(2.5 * cm, y, "- None")
    else:
        for s in risk_suppliers:
            c.drawString(
                2.5 * cm,
                y,
                f"- {s['supplier']} | 48h: {s['on_time_48h']}% | Return: {s['return_rate']}%"
            )
            y -= 0.6 * cm

    c.showPage()
    c.save()