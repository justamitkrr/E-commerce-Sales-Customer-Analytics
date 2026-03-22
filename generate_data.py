import pandas as pd
import numpy as np
import os

np.random.seed(7)
n = 50000

order_ids    = [f"ORD{str(i).zfill(6)}" for i in range(1, n+1)]
customer_ids = [f"CUST{np.random.randint(1000,9999)}" for _ in range(n)]

categories   = np.random.choice(["Electronics","Fashion","Home & Kitchen","Beauty","Sports","Books","Toys","Grocery"], n,
               p=[0.20,0.22,0.15,0.12,0.08,0.07,0.06,0.10])
sub_cats = {
    "Electronics":   ["Mobile","Laptop","Earphones","Tablet","Camera"],
    "Fashion":       ["Men Clothing","Women Clothing","Footwear","Accessories","Bags"],
    "Home & Kitchen":["Cookware","Furniture","Decor","Bedding","Cleaning"],
    "Beauty":        ["Skincare","Haircare","Makeup","Fragrance","Wellness"],
    "Sports":        ["Fitness","Cricket","Football","Yoga","Cycling"],
    "Books":         ["Fiction","Non-Fiction","Academic","Comics","Children"],
    "Toys":          ["Board Games","Action Figures","Outdoor","Educational","Dolls"],
    "Grocery":       ["Snacks","Beverages","Dairy","Grains","Organic"],
}
sub_category = [np.random.choice(sub_cats[c]) for c in categories]

cities       = np.random.choice(["Mumbai","Delhi","Bangalore","Hyderabad","Chennai","Pune","Kolkata","Ahmedabad"], n,
               p=[0.18,0.20,0.17,0.10,0.10,0.08,0.09,0.08])
regions      = {"Mumbai":"West","Delhi":"North","Bangalore":"South","Hyderabad":"South",
                "Chennai":"South","Pune":"West","Kolkata":"East","Ahmedabad":"West"}
region       = [regions[c] for c in cities]

start        = pd.Timestamp("2023-01-01")
order_dates  = [start + pd.Timedelta(days=int(x)) for x in np.random.randint(0, 730, n)]

price_map    = {"Electronics":15000,"Fashion":1200,"Home & Kitchen":2500,"Beauty":800,
                "Sports":1500,"Books":400,"Toys":600,"Grocery":300}
base_prices  = np.array([price_map[c] for c in categories])
unit_price   = np.round(base_prices * np.random.uniform(0.5, 2.5, n), 2)
quantity     = np.random.choice([1,2,3,4,5], n, p=[0.55,0.25,0.10,0.06,0.04])
discount_pct = np.random.choice([0,5,10,15,20,25,30], n, p=[0.20,0.15,0.20,0.18,0.12,0.10,0.05])
sales        = np.round(unit_price * quantity * (1 - discount_pct/100), 2)
cost_pct     = {"Electronics":0.70,"Fashion":0.45,"Home & Kitchen":0.55,"Beauty":0.40,
                "Sports":0.50,"Books":0.35,"Toys":0.42,"Grocery":0.65}
cost         = np.round(sales * np.array([cost_pct[c] for c in categories]), 2)
profit       = np.round(sales - cost, 2)

payment      = np.random.choice(["UPI","Credit Card","Debit Card","COD","Net Banking"], n,
               p=[0.35,0.22,0.18,0.15,0.10])
status_vals  = np.random.choice(["Delivered","Returned","Cancelled","Pending"], n,
               p=[0.78,0.10,0.08,0.04])
ratings      = np.where(np.array(status_vals)=="Delivered",
               np.random.choice([1,2,3,4,5], n, p=[0.03,0.07,0.15,0.40,0.35]), np.nan)

df = pd.DataFrame({
    "order_id":     order_ids,
    "customer_id":  customer_ids,
    "order_date":   [d.date() for d in order_dates],
    "category":     categories,
    "sub_category": sub_category,
    "city":         cities,
    "region":       region,
    "unit_price":   unit_price,
    "quantity":     quantity,
    "discount_pct": discount_pct,
    "sales":        sales,
    "cost":         cost,
    "profit":       profit,
    "payment_mode": payment,
    "order_status": status_vals,
    "rating":       ratings,
})

os.makedirs("data", exist_ok=True)
df.to_csv("data/ecommerce_orders.csv", index=False)
print(f"Dataset saved: {len(df)} rows")
print(df.head(3).to_string())
