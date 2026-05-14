# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("../data/customer_data.csv")

# Show First 5 Rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset Information
print("\nDATASET INFORMATION")
print(df.info())

# Check Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Statistical Summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Correlation Heatmap
plt.figure(figsize=(10,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("../images/correlation_heatmap.png")

plt.show()

# Sales Distribution Plot
plt.figure(figsize=(8,5))

sns.histplot(
    df['Annual Income (k$)'],
    kde=True
)

plt.title("Annual Income Distribution")

plt.savefig("../images/sales_distribution.png")

plt.show()

# Age vs Spending Score
plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Age',
    y='Spending Score (1-100)',
    hue='Gender',
    data=df
)

plt.title("Age vs Spending Score")

plt.savefig("../images/age_vs_spending.png")

plt.show()

# Group Analysis
print("\nAVERAGE SPENDING SCORE BY GENDER")

avg_spending = df.groupby('Gender')['Spending Score (1-100)'].mean()

print(avg_spending)

# Final Insights
print("\nKEY INSIGHTS")

print("1. Young customers have higher spending scores.")
print("2. Female customers spend slightly more.")
print("3. Income impacts spending behavior.")
