### Project 2: Exploratory Data Analysis Insights

**1. Problem Statement**
To analyze the provided dataset of 1200 records, identify underlying patterns, detect statistical anomalies using the IQR method, and map linear relationships to drive business intelligence.

**2. Methodology**
* Conducted univariate analysis using a Five-Number Summary.
* Applied the Interquartile Range (IQR) method to detect outliers.
* Utilized the Pearson Correlation Coefficient to map relationships.

**3. Key Findings**
* **Distribution Check (TotalPrice):** The median value is 823.62, while the maximum value reaches 3456.40.
* **Outlier Detection (IQR Method):**
*   **Quantity**: 0 outliers detected.
*   **UnitPrice**: 0 outliers detected.
*   **ItemsInCart**: 0 outliers detected.
*   **TotalPrice**: 8 outliers detected.
* **Strongest Driver:** The most significant relationship exists between **UnitPrice** and **TotalPrice** with a correlation coefficient of **0.72**.

**4. Recommendations**
* **Investigate Outliers:** Review the flagged outliers in the columns above to determine if they represent actionable business signals (e.g., VIP behaviour) or data entry noise.
* **Leverage Key Drivers:** Utilize the strong correlation between UnitPrice and TotalPrice to inform operational and marketing strategies.
