import pandas as pd

df = pd.read_excel('Dataset for Data Analytics_2.xlsx')

print('--- Five-Number Summary ---')
print(df.describe().round(2))

# --- Outlier Detection ---
numeric_cols = df.select_dtypes(include='number')
print('\n--- Outlier Detection ---')
outlier_details = []
for col in numeric_cols.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outliers_count = len(outliers)
    outlier_details.append(f"*   **{col}**: {outliers_count} outliers detected.")
    print(f"{col}: {len(outliers)} suspects found")

outlier_text = "\n".join(outlier_details)

# --- Correlation Analysis ---
print('\n--- Pearson Correlation Matrix ---')
corr_matrix = numeric_cols.corr()
corr_pairs = corr_matrix.unstack().sort_values(key=abs, ascending=False)
corr_pairs = corr_pairs[corr_pairs < 0.999]
top_pair = corr_pairs.index[0]
top_val = corr_pairs.iloc[0]
print(corr_matrix.round(2))

total_rows = len(df)
target_col = numeric_cols.columns[-1]
target_median = numeric_cols[target_col].median()
target_max = numeric_cols[target_col].max()

# --- Generate Executive Summary Report ---

summary_content = f"""### Project 2: Exploratory Data Analysis Insights

**1. Problem Statement**
To analyze the provided dataset of {total_rows} records, identify underlying patterns, detect statistical anomalies using the IQR method, and map linear relationships to drive business intelligence.

**2. Methodology**
* Conducted univariate analysis using a Five-Number Summary.
* Applied the Interquartile Range (IQR) method to detect outliers.
* Utilized the Pearson Correlation Coefficient to map relationships.

**3. Key Findings**
* **Distribution Check ({target_col}):** The median value is {target_median:.2f}, while the maximum value reaches {target_max:.2f}.
* **Outlier Detection (IQR Method):**
{outlier_text}
* **Strongest Driver:** The most significant relationship exists between **{top_pair[0]}** and **{top_pair[1]}** with a correlation coefficient of **{top_val:.2f}**.

**4. Recommendations**
* **Investigate Outliers:** Review the flagged outliers in the columns above to determine if they represent actionable business signals (e.g., VIP behaviour) or data entry noise.
* **Leverage Key Drivers:** Utilize the strong correlation between {top_pair[0]} and {top_pair[1]} to inform operational and marketing strategies.
"""

with open("EDA_Executive_Summary.md", "w", encoding="utf-8") as file:
    file.write(summary_content)
print(f"\nSuccess: EDA Executive Summary generated for {total_rows} records and saved as 'EDA_Executive_Summary.md'")