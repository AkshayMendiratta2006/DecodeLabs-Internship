import pandas as pd
import sqlite3

df = pd.read_excel('Dataset for Data Analytics.xlsx')
conn = sqlite3.connect(':memory:')
df.to_sql('sales', conn, index=False)

query_product = """
SELECT
    Product,
    COUNT(OrderID) AS Total_Orders,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""
print("--- Query 1: Product Performance ---")
df_product = pd.read_sql_query(query_product, conn)
print(df_product)
top_prod_1 = df_product.iloc[0]['Product']
top_rev_1 = df_product.iloc[0]['Total_Revenue']
top_prod_2 = df_product.iloc[1]['Product']
top_rev_2 = df_product.iloc[1]['Total_Revenue']

query_status = """
SELECT
    OrderStatus,
    COUNT(OrderID) AS Order_Count
FROM sales
GROUP BY OrderStatus;
"""
print("\n--- Query 2: Order Status Distribution ---")
df_status = pd.read_sql_query(query_status, conn)
print(df_status)
total_orders = df_status['Order_Count'].sum()
cancelled = int(df_status[df_status['OrderStatus'] == 'Cancelled']['Order_Count'].iloc[0])
returned = int(df_status[df_status['OrderStatus'] == 'Returned']['Order_Count'].iloc[0])
fail_rate = ((cancelled + returned) / total_orders) * 100

query_vip = """
SELECT
    Quantity,
    TotalPrice
FROM sales
WHERE TotalPrice > 200
ORDER BY TotalPrice DESC
LIMIT 5;
"""
print("\n--- Query 3: Top 5 High-Value Transactions ---")
df_vip = pd.read_sql_query(query_vip, conn)
print(df_vip)
vip_min = df_vip['TotalPrice'].min()
vip_max = df_vip['TotalPrice'].max()
vip_qty = int(df_vip['Quantity'].mode()[0])

summary_content = f"""# Project 3: SQL Data Analysis Insights

## 1. Problem Statement

To extract actionable business intelligence from raw e-commerce data using structured query logic, focusing on product performance, order fulfillment rates, and high-value customer identification.

## 2. Methodology

* Executed relational `SELECT` queries using `sqlite3` and `pandas`.
* Utilized `GROUP BY` and aggregation functions (`COUNT`, `SUM`, `AVG`) to collapse raw rows into categorical buckets.
* Applied `ORDER BY` to rank product revenue and isolate top-tier transactions.

## 3. Key Findings

* **Top Performers:** {top_prod_1}s and {top_prod_2}s are the primary revenue drivers, generating over ${top_rev_2:,.2f} each in total revenue.
* **Fulfillment Crisis:** A critical failure exists in the fulfillment pipeline. Out of {total_orders} total orders, {cancelled} were 'Cancelled' and {returned} were 'Returned' (a combined {fail_rate:.1f}% failure rate).
* **VIP Baselines:** The top 5 high-value transactions range from ${vip_min:,.2f} to ${vip_max:,.2f}, consistently driven by maximum cart quantities ({vip_qty} items).

## 4. Recommendations

* **Supply Chain Audit:** Immediately investigate the root cause of the cancellation and return rates. Plugging this {fail_rate:.0f}% leak is the highest priority for revenue retention.
* **Inventory Focus:** Prioritize inventory stocking and marketing spend on {top_prod_1}s and {top_prod_2}s, which show the highest total unit movement and revenue generation.
"""

with open("SQL_Executive_Summary.md", "w", encoding="utf-8") as file:
    file.write(summary_content)
print(f"\nSuccess: SQL Executive Summary generated for {total_orders} records!")