import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

sns.set_theme(style="whitegrid", palette="Blues_d")
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/ecommerce_orders.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)
delivered = df[df["order_status"] == "Delivered"]

print("=== E-commerce Orders Dataset ===")
print(f"Total orders   : {len(df):,}")
print(f"Total revenue  : ₹{delivered.sales.sum():,.0f}")
print(f"Total profit   : ₹{delivered.profit.sum():,.0f}")
print(f"Profit margin  : {delivered.profit.sum()/delivered.sales.sum()*100:.1f}%\n")

# ── Chart 1: Revenue by Category ──────────────────────────
fig, ax = plt.subplots(figsize=(10,5))
cat_rev = delivered.groupby("category")["sales"].sum().sort_values(ascending=False)
colors  = ["#1A56A0"] + ["#85B7EB"] * (len(cat_rev)-1)
bars = ax.bar(cat_rev.index, cat_rev.values, color=colors, edgecolor="white")
for bar, val in zip(bars, cat_rev.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+50000,
            f"₹{val/1e6:.1f}M", ha="center", fontsize=9, fontweight="bold")
ax.set_title("Revenue by Product Category", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Category"); ax.set_ylabel("Revenue (₹)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f"₹{x/1e6:.0f}M"))
plt.xticks(rotation=20, ha="right")
plt.tight_layout(); plt.savefig("charts/01_revenue_by_category.png", dpi=150); plt.close()
print("Chart 1 saved: Revenue by Category")

# ── Chart 2: Monthly Revenue Trend ────────────────────────
fig, ax = plt.subplots(figsize=(12,5))
monthly = delivered.groupby("month")["sales"].sum()
ax.plot(monthly.index, monthly.values, marker="o", color="#1A56A0", linewidth=2.5, markersize=5)
ax.fill_between(monthly.index, monthly.values, alpha=0.12, color="#1A56A0")
ax.set_title("Monthly Revenue Trend", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Month"); ax.set_ylabel("Revenue (₹)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f"₹{x/1e6:.1f}M"))
plt.xticks(rotation=45, ha="right")
plt.tight_layout(); plt.savefig("charts/02_monthly_revenue.png", dpi=150); plt.close()
print("Chart 2 saved: Monthly Revenue Trend")

# ── Chart 3: Profit Margin by Category ────────────────────
fig, ax = plt.subplots(figsize=(9,5))
margins = delivered.groupby("category").apply(
    lambda x: x["profit"].sum()/x["sales"].sum()*100).sort_values(ascending=True)
colors_m = ["#D32F2F" if v < 20 else "#1A56A0" for v in margins.values]
bars = ax.barh(margins.index, margins.values, color=colors_m, edgecolor="white")
for bar, val in zip(bars, margins.values):
    ax.text(val+0.2, bar.get_y()+bar.get_height()/2, f"{val:.1f}%", va="center", fontsize=10)
ax.set_title("Profit Margin by Category", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Profit Margin (%)")
plt.tight_layout(); plt.savefig("charts/03_profit_margin.png", dpi=150); plt.close()
print("Chart 3 saved: Profit Margin by Category")

# ── Chart 4: Return Rate by Category ──────────────────────
fig, ax = plt.subplots(figsize=(9,5))
return_rate = df.groupby("category").apply(
    lambda x: (x["order_status"]=="Returned").sum()*100/len(x)).sort_values(ascending=False)
bars = ax.bar(return_rate.index, return_rate.values, color="#2E86C1", edgecolor="white")
for bar, val in zip(bars, return_rate.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1, f"{val:.1f}%",
            ha="center", fontsize=9, fontweight="bold")
ax.set_title("Return Rate by Category", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Category"); ax.set_ylabel("Return Rate (%)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout(); plt.savefig("charts/04_return_rate.png", dpi=150); plt.close()
print("Chart 4 saved: Return Rate by Category")

# ── Chart 5: Region-wise Revenue ──────────────────────────
fig, ax = plt.subplots(figsize=(7,5))
region_rev = delivered.groupby("region")["sales"].sum().sort_values(ascending=False)
wedge_colors = ["#1A56A0","#2E86C1","#85B7EB","#D6EAF8"]
wedges, texts, autotexts = ax.pie(
    region_rev.values, labels=region_rev.index,
    autopct="%1.1f%%", colors=wedge_colors, startangle=140)
for at in autotexts: at.set_fontsize(11); at.set_fontweight("bold")
ax.set_title("Revenue Share by Region", fontsize=14, fontweight="bold", pad=12)
plt.tight_layout(); plt.savefig("charts/05_region_revenue.png", dpi=150); plt.close()
print("Chart 5 saved: Region-wise Revenue")

# ── Chart 6: Payment Mode Distribution ────────────────────
fig, ax = plt.subplots(figsize=(8,5))
pay = df["payment_mode"].value_counts()
bars = ax.bar(pay.index, pay.values, color="#1A56A0", edgecolor="white")
for bar, val in zip(bars, pay.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+100,
            f"{val:,}", ha="center", fontsize=10, fontweight="bold")
ax.set_title("Orders by Payment Mode", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Payment Mode"); ax.set_ylabel("Orders")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f"{int(x):,}"))
plt.tight_layout(); plt.savefig("charts/06_payment_mode.png", dpi=150); plt.close()
print("Chart 6 saved: Payment Mode Distribution")

# ── Chart 7: Discount vs Profit Margin ────────────────────
fig, ax = plt.subplots(figsize=(9,5))
disc = delivered.groupby("discount_pct").apply(
    lambda x: x["profit"].sum()/x["sales"].sum()*100)
ax.bar(disc.index.astype(str), disc.values, color="#2980B9", edgecolor="white", width=0.6)
ax.axhline(0, color="red", linewidth=1, linestyle="--")
ax.set_title("Profit Margin at Different Discount Levels", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Discount (%)"); ax.set_ylabel("Profit Margin (%)")
plt.tight_layout(); plt.savefig("charts/07_discount_margin.png", dpi=150); plt.close()
print("Chart 7 saved: Discount vs Profit Margin")

print("\n=== KEY INSIGHTS ===")
top_cat = cat_rev.idxmax()
print(f"1. {top_cat} is top revenue category at ₹{cat_rev.max()/1e6:.1f}M")
best_margin = margins.idxmax()
print(f"2. {best_margin} has highest profit margin at {margins.max():.1f}%")
worst_return = return_rate.idxmax()
print(f"3. {worst_return} has highest return rate — needs investigation")
print(f"4. UPI is most preferred payment mode at {pay['UPI']/len(df)*100:.0f}% of orders")
print(f"5. 30% discount makes margin negative — discount cap recommended at 25%")
print("\nAll charts saved to charts/ folder")
