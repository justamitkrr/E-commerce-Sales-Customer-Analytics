-- ============================================================
-- PROJECT 2: E-commerce Sales & Customer Analytics
-- Tool: MySQL / SQLite
-- Run after importing ecommerce_orders.csv into your DB
-- ============================================================

-- QUERY 1: Total revenue, profit and margin by category
SELECT
    category,
    COUNT(*)                             AS total_orders,
    ROUND(SUM(sales), 0)                 AS total_revenue,
    ROUND(SUM(profit), 0)                AS total_profit,
    ROUND(SUM(profit)*100.0/SUM(sales),1) AS profit_margin_pct
FROM ecommerce_orders
WHERE order_status = 'Delivered'
GROUP BY category
ORDER BY total_revenue DESC;


-- QUERY 2: Monthly revenue trend
SELECT
    SUBSTR(order_date, 1, 7)  AS month,
    COUNT(*)                  AS orders,
    ROUND(SUM(sales), 0)      AS revenue,
    ROUND(SUM(profit), 0)     AS profit
FROM ecommerce_orders
WHERE order_status = 'Delivered'
GROUP BY month
ORDER BY month;


-- QUERY 3: Region-wise performance
SELECT
    region,
    COUNT(DISTINCT customer_id)          AS unique_customers,
    COUNT(*)                             AS total_orders,
    ROUND(SUM(sales), 0)                 AS revenue,
    ROUND(AVG(sales), 0)                 AS avg_order_value
FROM ecommerce_orders
WHERE order_status = 'Delivered'
GROUP BY region
ORDER BY revenue DESC;


-- QUERY 4: Top 10 cities by revenue
SELECT
    city,
    COUNT(*)                  AS orders,
    ROUND(SUM(sales), 0)      AS revenue,
    ROUND(AVG(rating), 2)     AS avg_rating
FROM ecommerce_orders
WHERE order_status = 'Delivered'
GROUP BY city
ORDER BY revenue DESC
LIMIT 10;


-- QUERY 5: Customer segmentation by purchase frequency
SELECT
    purchase_segment,
    COUNT(*) AS customers
FROM (
    SELECT
        customer_id,
        COUNT(*) AS orders,
        CASE
            WHEN COUNT(*) >= 10 THEN 'High Value'
            WHEN COUNT(*) >= 5  THEN 'Medium Value'
            ELSE 'Low Value'
        END AS purchase_segment
    FROM ecommerce_orders
    WHERE order_status = 'Delivered'
    GROUP BY customer_id
) t
GROUP BY purchase_segment;


-- QUERY 6: Return rate by category
SELECT
    category,
    COUNT(*)                                                              AS total_orders,
    SUM(CASE WHEN order_status='Returned' THEN 1 ELSE 0 END)             AS returns,
    ROUND(SUM(CASE WHEN order_status='Returned' THEN 1 ELSE 0 END)*100.0/COUNT(*),1) AS return_rate_pct
FROM ecommerce_orders
GROUP BY category
ORDER BY return_rate_pct DESC;


-- QUERY 7: Payment mode preference
SELECT
    payment_mode,
    COUNT(*)                              AS orders,
    ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(),1) AS pct
FROM ecommerce_orders
GROUP BY payment_mode
ORDER BY orders DESC;


-- QUERY 8: Discount impact on profit margin
SELECT
    discount_pct,
    COUNT(*)                             AS orders,
    ROUND(AVG(profit), 0)                AS avg_profit,
    ROUND(SUM(profit)*100.0/SUM(sales),1) AS profit_margin_pct
FROM ecommerce_orders
WHERE order_status='Delivered'
GROUP BY discount_pct
ORDER BY discount_pct;


-- QUERY 9: Top 20% customers by revenue (Pareto check)
SELECT
    ROUND(SUM(revenue)*100.0/(SELECT SUM(sales) FROM ecommerce_orders WHERE order_status='Delivered'), 1) AS top20_revenue_pct
FROM (
    SELECT customer_id, SUM(sales) AS revenue
    FROM ecommerce_orders
    WHERE order_status='Delivered'
    GROUP BY customer_id
    ORDER BY revenue DESC
    LIMIT (SELECT CAST(COUNT(DISTINCT customer_id)*0.2 AS INT) FROM ecommerce_orders)
) top_customers;


-- QUERY 10: Weekend vs weekday orders (SQLite: strftime)
SELECT
    CASE WHEN CAST(strftime('%w', order_date) AS INT) IN (0,6) THEN 'Weekend' ELSE 'Weekday' END AS day_type,
    COUNT(*)              AS orders,
    ROUND(SUM(sales), 0)  AS revenue
FROM ecommerce_orders
WHERE order_status='Delivered'
GROUP BY day_type;
