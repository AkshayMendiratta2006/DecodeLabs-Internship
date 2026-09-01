# Project 3: SQL Data Analysis Insights

## 1. Problem Statement

To extract actionable business intelligence from raw e-commerce data using structured query logic, focusing on product performance, order fulfillment rates, and high-value customer identification.

## 2. Methodology

* Executed relational `SELECT` queries using `sqlite3` and `pandas`.
* Utilized `GROUP BY` and aggregation functions (`COUNT`, `SUM`, `AVG`) to collapse raw rows into categorical buckets.
* Applied `ORDER BY` to rank product revenue and isolate top-tier transactions.

## 3. Key Findings

* **Top Performers:** Chairs and Printers are the primary revenue drivers, generating over $195,612.61 each in total revenue.
* **Fulfillment Crisis:** A critical failure exists in the fulfillment pipeline. Out of 1200 total orders, 250 were 'Cancelled' and 247 were 'Returned' (a combined 41.4% failure rate).
* **VIP Baselines:** The top 5 high-value transactions range from $3,370.20 to $3,456.40, consistently driven by maximum cart quantities (5 items).

## 4. Recommendations

* **Supply Chain Audit:** Immediately investigate the root cause of the cancellation and return rates. Plugging this 41% leak is the highest priority for revenue retention.
* **Inventory Focus:** Prioritize inventory stocking and marketing spend on Chairs and Printers, which show the highest total unit movement and revenue generation.
