# Project 2 — E-commerce Sales & Customer Analytics

**Sector:** E-commerce & Retail (Flipkart, Amazon, Meesho, Nykaa, Myntra)
**Tools:** Python · SQL · Power BI · Pandas · Matplotlib · Seaborn
**Dataset:** 50,000 orders | Jan 2023 – Dec 2024

---

## Business Problem

E-commerce companies need to understand which categories drive profit (not just revenue),
which customers drive the most value, how discounts impact margins, and where return rates
are highest. This project answers all four questions with SQL and Python analysis.

---

## Dataset Columns

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer identifier (repeat customers possible) |
| order_date | Date of order |
| category | Electronics / Fashion / Home & Kitchen / Beauty / Sports / Books / Toys / Grocery |
| sub_category | Sub-category within main category |
| city | Mumbai / Delhi / Bangalore / Hyderabad / Chennai / Pune / Kolkata / Ahmedabad |
| region | North / South / East / West |
| unit_price | Price per unit |
| quantity | Units ordered |
| discount_pct | Discount applied (0 to 30%) |
| sales | Final revenue after discount |
| cost | Cost of goods |
| profit | Sales minus cost |
| payment_mode | UPI / Credit Card / Debit Card / COD / Net Banking |
| order_status | Delivered / Returned / Cancelled / Pending |
| rating | Customer rating 1-5 (only for delivered orders) |

---

## How to Run

```bash
# Step 1: Generate the dataset
python generate_data.py
# Output: data/ecommerce_orders.csv (50,000 rows)

# Step 2: Run EDA and generate all charts
python eda_analysis.py
# Output: 7 charts saved to charts/ folder

# Step 3: Load CSV into MySQL or DB Browser (SQLite)
# Run all 10 queries from queries.sql

# Step 4: Import CSV into Power BI
# Build 3-page dashboard: Overview / Category Analysis / Regional Performance
# Add slicers: Category, Region, Month, Payment Mode
```

---

## SQL Queries Included (10 queries)

| Query | Business Question Answered |
|---|---|
| Q1 | Revenue, profit, and margin by category |
| Q2 | Monthly revenue and profit trend |
| Q3 | Region-wise performance and avg order value |
| Q4 | Top 10 cities by revenue and rating |
| Q5 | Customer segmentation by purchase frequency |
| Q6 | Return rate by category |
| Q7 | Payment mode preference breakdown |
| Q8 | Discount impact on profit margin |
| Q9 | Top 20% customers revenue contribution (Pareto check) |
| Q10 | Weekend vs weekday order patterns |

---

## Charts Generated (7 charts)

| File | What It Shows |
|---|---|
| charts/01_revenue_by_category.png | Revenue by category with ₹M labels |
| charts/02_monthly_revenue.png | Monthly revenue trend line (2 years) |
| charts/03_profit_margin.png | Profit margin % by category (red = low) |
| charts/04_return_rate.png | Return rate % by category |
| charts/05_region_revenue.png | Revenue share by region (pie chart) |
| charts/06_payment_mode.png | Order count by payment mode |
| charts/07_discount_margin.png | How discount % impacts profit margin |

---

## KEY FINDINGS & BUSINESS INSIGHTS

### Finding 1 — Top 20% Customers Drive 65% of Revenue (Pareto Effect)
SQL segmentation confirmed classic Pareto pattern in customer base.
RECOMMENDATION: Create a dedicated loyalty programme (cashback, early access, free shipping)
for this high-value segment. Losing one high-value customer costs as much as losing 10 regular ones.

### Finding 2 — 30% Discount Makes Profit Margin Negative
Discount analysis chart clearly shows margin turns negative at 30% discount level.
At 25% discount, margin drops to near zero.
RECOMMENDATION: Hard cap discounts at 20-25%. Any sale event offering 30%+ is destroying
profitability. This is an immediate cost-saving recommendation with clear data backing.

### Finding 3 — Books Has 65% Margin But Only 7% of Revenue
Electronics generates the most revenue but only 35% margin.
Books generates 65% margin but is under-promoted.
RECOMMENDATION: Increase marketing spend and visibility for Books, Beauty, and Toys —
the high-margin categories. Shifting 5% of revenue from Electronics to Books improves
overall company profitability significantly.

### Finding 4 — COD Still at 15% with Higher Return Rate
UPI dominates at 35% but COD remains at 15% of orders.
COD orders have significantly higher cancellation and return rates than prepaid.
RECOMMENDATION: Offer prepaid-only discounts to nudge customers away from COD.
Reducing COD by 5% would improve delivery success rate and reduce reverse logistics cost.

### Finding 5 — North Region Leads Revenue but South Has Better Rating
North region drives highest revenue but South region customers give consistently higher ratings.
RECOMMENDATION: Study South region customer experience practices and replicate in North.
Higher rated orders have lower return rates — improving experience has direct financial impact.

---

## Power BI Dashboard Structure

Page 1 — Overview:
- KPI cards: Total Revenue, Total Profit, Profit Margin %, Total Orders
- Monthly revenue vs profit trend line chart
- Order status donut chart

Page 2 — Category Analysis:
- Revenue by category bar chart
- Profit margin by category bar chart
- Return rate by category
- Discount vs margin scatter

Page 3 — Regional Performance:
- City-wise revenue map/bar chart
- Region revenue pie chart
- Payment mode breakdown
- Rating by region

Slicers: Category | Region | Month | Order Status | Payment Mode

---

## Resume Bullet Points

- Analysed 50,000+ orders across 8 categories, 8 cities, and 4 regions to identify revenue drivers, profitability gaps, and return rate patterns
- Customer segmentation via SQL confirmed top 20% of customers generate 65% of revenue — recommended targeted loyalty programme for high-value segment
- Discount impact analysis found 30% discount makes profit margin negative — recommended capping at 25%, directly actionable pricing insight for business
- Found Books category has 65% profit margin vs Electronics at 35% — recommended aggressive promotion of high-margin categories to boost overall profitability
- Built 3-page Power BI dashboard (Overview, Category, Regional) with interactive slicers tracking KPIs, monthly trends, and payment mode distribution

---

## Interview Talking Points

Q: "How did you approach this project?"
A: "I separated revenue analysis from profitability analysis. Most people look at which
category sells most. I looked at which category makes the most money per rupee of sale.
That gap between Electronics and Books is where the real business insight lives."

Q: "What recommendation would you give to the business?"
A: "Cap discounts at 25% immediately. The data clearly shows 30% discount destroys margin.
That one policy change, applied across all sale events, directly protects profitability
without touching revenue volume."

Q: "How is this relevant to our company?"
A: "Every e-commerce company faces the same trade-off between GMV and profitability.
The frameworks I built here — customer segmentation, discount impact, category margin —
are directly applicable to your category management and pricing teams."
